# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If tree is empty, it is symmetric
        if not root:
            return True

        # Use a queue to store pairs of nodes for comparison
        queue = [root.left, root.right]

        # Process until queue is empty
        while queue:
            # Pop two nodes at a time (they should be mirror images)
            t1 = queue.pop(0)
            t2 = queue.pop(0)

            # If both are None, continue to next pair
            if not t1 and not t2:
                continue

            # If only one is None OR values don't match → not symmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False

            # Add children in mirrored order:
            # Left child of t1 with Right child of t2
            queue.append(t1.left)
            queue.append(t2.right)

            # Right child of t1 with Left child of t2
            queue.append(t1.right)
            queue.append(t2.left)

        # If all pairs matched → symmetric
        return True
