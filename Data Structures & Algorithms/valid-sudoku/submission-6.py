class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = [{} for _ in range(10)]
        d1 = [[{} for j in range(3)] for i in range(3)]
        for i in range(9):
            dj={}
            for j in range(9):
                num =board[i][j]
                if num == ".":
                    continue
                if num in dj:
                    return False
                else: 
                    dj[num]=1
                if num in d[j]:
                    return False
                else: 
                    d[j][num]=1
                if num in d1[i//3][j//3]:
                    return False
                else: 
                    d1[i//3][j//3][num] = 1
        return True

                
                


        