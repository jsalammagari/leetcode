# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def nodeTraverse(node: Optional[TreeNode]):
        #     if p and not q:
        #         return False
        #     if not p and q:
        #         return False
        #     if
        #     if p and q:
        #         node1= [p.val]+[nodeTraverse(p.left)]+[nodeTraverse(p.right)]
        #         node2= [q.val]+[nodeTraverse(q.left)]+[nodeTraverse(q.right)]
        #         if node1==node2:
        #             return True
        if p and not q:
            return False
        if not p and q:
            return False
        if not p and not q:
            return True
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
                

        