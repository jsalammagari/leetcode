# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafNodes(node : Optional[TreeNode]):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return leafNodes(node.left)+leafNodes(node.right)
        leaves1 = leafNodes(root1)
        leaves2 = leafNodes(root2)
        return leaves1==leaves2
             