class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, total = 0, 0, 0
        length = len(nums) + 1

        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target:
                length = min(length, right-left)
                total -= nums[left]
                left += 1
        if length == len(nums) + 1:
            return 0
        else:
            return length
        
