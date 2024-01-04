class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = [char.lower() for char in s if char.isalnum()]
        l = 0
        r = len(ls)-1
        while l<r:
            if ls[l] != ls[r]:
                return False
            l += 1
            r -= 1
        return True
