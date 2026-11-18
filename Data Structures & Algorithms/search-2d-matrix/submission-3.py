class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        lo=0
        hi=m*n-1
        while lo<=hi:
            g = (hi+lo)//2
            V=matrix[g//n][g%n]
            if V ==target:return True
            elif V>target:hi=g-1
            else:lo=g+1
        return False





        