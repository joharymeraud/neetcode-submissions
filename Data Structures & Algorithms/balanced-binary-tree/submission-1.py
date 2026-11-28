# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ecart=0
        def dfs(n):
            nonlocal ecart 
            if n==None:
                return 0
            else:
                left=dfs(n.left)
                right=dfs(n.right)

                if ecart <=1:
                    ecart=abs(right-left)

                return 1+max(left,right)
        dfs(root)
        if ecart >1:
            return False
        return True 
        



                
        
        