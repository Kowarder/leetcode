class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        l = list(zip(*strs))

        for i in l:
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s
