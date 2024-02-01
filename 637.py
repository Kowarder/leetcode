# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []
        ans = []
        queue.append(root)
        while (queue):
            qlen = len(queue)
            temp = 0
            for i in range(qlen):
                curr = queue.pop(0)
                temp += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(temp/qlen)
        return ans
