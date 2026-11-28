# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h=0
        d={}
        liste = deque()
        liste.append(root)
        final=None
        while liste:
            for i in range(len(liste)):
                node=liste.popleft()
                if node:
                    liste.append(node.right)
                    liste.append(node.left)
                    if node.right:
                        if node not in d:
                            d[node]=[node.right]
                        else:
                            d[node].append(node.right)
                        d[node.right]=[node]
                    if node.left:
                        if node not in d:
                            d[node]=[node.left]
                        else:
                            d[node].append(node.left)
                        d[node.left]=[node]
                    final=node
            
        #maintenant qu'on a le dernier node et la liste d'adj on refait un BFS:

        bfs=deque()
        bfs.append(final)

        visited=set()
        visited.add(final)

        h=0

        if len(d)==0:
            return 0

        while bfs:
            for i in range(len(bfs)):
                node=bfs.popleft()
                if node:
                    for voisin in d[node]:
                        if voisin not in visited:
                            visited.add(voisin)
                            bfs.append(voisin)
            h+=1
        
        return h-1


        