class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ls = s.split()
        ls.reverse()
        return " ".join(ls)
