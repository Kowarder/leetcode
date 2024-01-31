# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}
        def dfs(root, lev):
            if not root:
                return None
            nonlocal ans
            dfs(root.right, lev+1)
            if lev not in ans:
                ans[lev] = root.val
            dfs(root.left, lev+1)
        dfs(root, 0)
        return [i for k, i in sorted(ans.items())]
