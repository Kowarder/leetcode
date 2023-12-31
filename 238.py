class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pre, post = 1, 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            result[j] *= post
            post *= nums[j]
        return result
