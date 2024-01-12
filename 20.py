class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[', '}':'{'}
        stk = []

        for i in s:
            if i in dic.values():
                stk.append(i)
            elif stk and dic[i] == stk[-1]:
                stk.pop()
            else:
                return False
        return stk == []
