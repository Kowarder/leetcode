class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.find(needle)
            return index
        except ValueError:
            return -1
