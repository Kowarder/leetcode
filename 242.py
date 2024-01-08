class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        for i, j in zip(ls, lt):
            if i != j:
                return False
        return True
