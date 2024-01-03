class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ls = s.split()
        last_word = ls.pop()
        return len(last_word)
