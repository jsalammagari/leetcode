# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.getLeaves(root1)
        leaves2 = self.getLeaves(root2)
        return leaves1 == leaves2
    def getLeaves(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        else:
            return self.getLeaves(root.left) + self.getLeaves(root.right)