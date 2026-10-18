class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        P = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    if j==0:
                        s=0
                        for k in range(i+1):
                            s+=matrix[k][j]
                        P[i][j]=s
                    else:
                        s=0
                        for k in range(j+1):
                            s+=matrix[i][k]
                        P[i][k]=s

                else:
                    P[i][j] = matrix[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
        self.P=P

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row2<row1 or col2<col1:
            return None

        s=self.P[row2][col2]
        if row1>=1:
            s-=self.P[row1-1][col2]
        if col1>=1:
            s-=self.P[row2][col1-1]
        if col1>=1 and row1>=1:
            s+=self.P[row1-1][col1-1]
        return s

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)