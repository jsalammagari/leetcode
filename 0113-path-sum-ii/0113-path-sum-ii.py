# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        path=[]
        self.getSelectedPath(root,targetSum,path,results)
        return results
    def getSelectedPath(self,root,targetSum,path,results):
        if not root:
            return None
        path.append(root.val)
        if (not root.left and not root.right) and sum(path)==targetSum:
            results.append(list(path))
        self.getSelectedPath(root.left,targetSum,path,results)
        self.getSelectedPath(root.right,targetSum,path,results)
        path.pop()