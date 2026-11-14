class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        ans = -float('inf')
        temp = 0
        while right < len(nums):
            temp += nums[right]
            ans = max(ans, temp)
            if temp < 0:
                temp = 0
                left = right
            right += 1
        return ans