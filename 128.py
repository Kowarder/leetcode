class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        r = 0
        for i in nums:
            if not i-1 in nums:
                length = 1
                while (i+1) in nums:
                    length += 1
                    i += 1
                r = max(r, length)
        return r
