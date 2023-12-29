class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        flag = len(nums)/2
        num = []
        cnt = 0
        for i in nums:
            if num.count(i) == 0:
                num.append(i)
        for j in num:
            if nums.count(j) > flag:
                return j
        return 0
