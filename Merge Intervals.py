class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        ans = []
        for item in intervals:
            if (item[0] >= left and item[0] <= right):
                right = max(right, item[1])
            else:
                ans.append([left, right])
                left = item[0]
                right = item[1]
        ans.append([left , right])
        return ans
