# This is a tough one to get first. But this isn't that hard. It's just a lot of edge case handling.


class Solution:
    def __init__(self):
        self.ans = []
    def backTracking(self, candidates, target, temp, start):
        if target < 0:
            return
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            if candidate <= target:
                value = target - candidate
                temp.append(candidate)
                if value == 0:
                    self.ans.append(temp.copy())
                    temp.pop()
                    return
                self.backTracking(candidates, value, temp, i)
                temp.pop()
            else:
                break

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        self.backTracking(candidates, target, [], 0)
        return self.ans