class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lm = list(magazine)
        for i in ransomNote:
            if i in lm:
                lm.remove(i)
            else:
                return False
        return True
