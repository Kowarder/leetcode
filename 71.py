class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i == '..':
                if stack:
                    stack.pop()
            elif i not in ('', '.'):
                stack.append(i)
        return '/' + '/'.join(stack)
