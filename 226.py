# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.result(root)
    def result(self, root):
        if(root == None) or (root.left == None and root.right == None):
            return root
        cache = root.right
        root.right = self.result(root.left)
        root.left = self.result(cache)
        return root
