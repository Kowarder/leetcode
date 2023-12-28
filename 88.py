class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Iterate through the two arrays from back to front.
        n_1 = m - 1
        n_2 = n - 1
        length = m + n - 1
        #Insert the nums2 to nums1, so when nums2's each number insert into nums1 end the loop
        while n_2 >= 0:
            
            if nums2[n_2] < nums1[n_1] and n_1 >= 0:
                nums1[length] = nums1[n_1]
                n_1 = n_1 - 1
                length = length - 1
            else:
                nums1[length] = nums2[n_2]
                n_2 = n_2 - 1
                length = length - 1
