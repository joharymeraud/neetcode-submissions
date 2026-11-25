# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        file = deque([root])
        h=0
        while file:
            for i in range(len(file)):
                node = file.popleft()
                if node:
                    file.append(node.left)
                    file.append(node.right)
            h+=1
        return h-1
            


        
        