class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[length-2]:
                nums[length] = nums[i]
                length += 1

        return length
