### Very good question for edge case handling practice
class Solution:
    def __init__(self):
        self.ans = [[]]
    def dfs(self, nums, temp, position):
        if position > len(nums):
            return
        for i in range(position, len(nums)):
            temp.append(nums[i])
            self.ans.append(temp.copy())
            self.dfs(nums, temp, i + 1)
            temp.pop()
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.dfs(nums, [], 0)
        return self.ans