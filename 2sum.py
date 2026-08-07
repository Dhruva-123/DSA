class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        ans = []
        for i,item in enumerate(nums):
            if target - item in seen:
                ans = [i,seen[target - item]]
                break
            else:
                seen[item] = i
        return ans
