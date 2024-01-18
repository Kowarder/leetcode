# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.result(root.left, root.right)
    def result(self, leftroot, rightroot):
        if leftroot is None and rightroot is None:
            return True
        if (leftroot is None and rightroot is not None) or (leftroot is not None and rightroot is None):
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.result(leftroot.left, rightroot.right) and self.result(leftroot.right, rightroot.left)
