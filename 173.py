# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.inorderTraversal(root)

    def next(self) -> int:
        if self.hasNext():
            return self.inorder.pop(0)

    def hasNext(self) -> bool:
        return bool(self.inorder)
    
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            self.inorder.append(root.val)
            self.inorderTraversal(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
