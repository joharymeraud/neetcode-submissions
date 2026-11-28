# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n1,n2):
            if n1==None and n2==None:
                return True
            elif n1==None or n2==None:
                return False
            else:
                sameleft=sameTree(n1.left,n2.left)
                sameright=sameTree(n1.right,n2.right)

                return (sameleft and sameright and n1.val==n2.val)
        
        liste=deque()
        liste.append(root)

        while liste:
            node=liste.pop()
            if node:
                liste.append(node.left)
                liste.append(node.right)

                if sameTree(node,subRoot): return True
        return False


        