# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        if abs(left_height - right_height)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self,root):
        if not root:
            return 0
        return max(1+self.height(root.left),(1+self.height(root.right)))