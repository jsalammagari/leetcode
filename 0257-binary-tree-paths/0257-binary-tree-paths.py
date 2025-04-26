# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        return self.getPaths(root,"",result)
    def getPaths(self,root,path,result):
        if not root:
            return None
        if not root.left and not root.right:
            result.append(path+str(root.val))
        if root.left:
            self.getPaths(root.left,path+str(root.val)+"->",result)
        if root.right:
            self.getPaths(root.right,path+str(root.val)+"->",result)
        return result