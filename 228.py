class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = 0
        while start < len(nums):
            begin = nums[start]
            while start < len(nums)-1 and nums[start] == nums[start+1]-1:
                start += 1
            end = nums[start]
            if begin == end:
                result.append(str(begin))
            else:
                result.append(str(begin)+"->"+str(end))
            start += 1

        return result
