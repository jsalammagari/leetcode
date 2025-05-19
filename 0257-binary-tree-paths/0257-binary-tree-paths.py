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
        self.getPaths(root,"",result)
        return result
    def getPaths(self,root,path,result):
        if not root:
            return None
        path = path+str(root.val)
        if not root.left and not root.right:
            result.append(path)
        else:
            path = path + "->"
            self.getPaths(root.left,path,result)
            self.getPaths(root.right,path,result)