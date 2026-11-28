# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        def dfs(n):
            nonlocal d 
            if n==None:
                return 0 
            else:
                left=dfs(n.left)
                right=dfs(n.right)
                d=max(d,left+right)
                return 1+max(left,right)
        dfs(root)
        return d
        


        