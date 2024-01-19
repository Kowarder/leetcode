class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 1:
            return [i for i in dic[digits]]
        else:
            l = []
            for i in digits:
                if i in dic.keys():
                    l.append(dic[i])
            if not l:
                return []
            result = [''.join(comb) for comb in product(*l)]
            return result
