class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r = {}
        for i, j in enumerate(nums):
            if j in r and abs(i-r[j]) <= k:
                return True
            else:
                r[j] = i
        return False
