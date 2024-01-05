class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        i, j = 0, 0
        if len(ls) == 0:
            return True
        while j < len(lt):
            if lt[j] == ls[i]:
                i += 1
                if i == len(ls):
                    break
            j += 1
        if i == len(ls):
            return True
        else:
            return False
