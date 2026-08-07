##### There isn't much going on here. It's just about cleverly using a for loop to get the answer flowing. 

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        prev = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if prev[1] >= intervals[i][0]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        return ans