class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {}
        dic_row = {}
        for row in board:
            row_cpy = row.copy()
            row_cpy = [x for x in row_cpy if x != '.']
            if len(set(row_cpy)) != len(row_cpy):
                return False
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                if str(i//3) + str(j//3) in dic:
                    dic[str(i//3) + str(j//3)].append(board[i][j])
                else:
                    dic[str(i//3) + str(j//3)] = [board[i][j]]

                if str(j) in dic_row:
                    dic_row[str(j)].append(board[i][j])
                else:
                    dic_row[str(j)] = [board[i][j]]
        for key in dic:
            if len(set(dic[key])) != len(dic[key]):
                print(key)
                return False

        for key in dic_row:
            if len(set(dic_row[key])) != len(dic_row[key]):
                print(key)
                return False
        return True
                
                
            
        