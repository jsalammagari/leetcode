# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_values(node: Optional[TreeNode]):
            if not node:
                return [];
            if not node.left and not node.right:
                return [node.val]
            return get_leaf_values(node.left)+get_leaf_values(node.right)
        leaves1=get_leaf_values(root1)
        leaves2=get_leaf_values(root2)
        return leaves1==leaves2