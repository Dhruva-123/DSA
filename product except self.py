class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]*len(nums)
        sufix = [1]*len(nums)
        ans = [1]*len(nums)
        temp = 1
        for i,item in enumerate(nums):
            prefix[i] *= temp
            temp *= item
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            sufix[i] *= temp
            temp *= nums[i]
        for i in range(len(nums)):
            ans[i] = prefix[i]*sufix[i]
        return ans


