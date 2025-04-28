# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)
    def dfs(self,root,current_sum):
        if not root:
            return 0
        current_sum = (2 * current_sum) + root.val
        if not root.left and not root.right:
            return current_sum
        return self.dfs(root.left,current_sum)+self.dfs(root.right,current_sum)