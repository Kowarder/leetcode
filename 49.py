class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in result:
                result[temp].append(i)
            else:
                result[temp] = [i]
        return result.values()
