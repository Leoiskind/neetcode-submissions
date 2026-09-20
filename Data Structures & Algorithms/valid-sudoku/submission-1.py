class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[[] for i in range(3)] for i in range(3)]
        cols = [[] for i in range(9)]
        for row in range(9):
            rowed = []
            for col in range(9):
                if board[row][col] == '.':
                    pass
                elif board[row][col] in rowed:
                    return False
                elif board[row][col] in cols[col]:
                    return False
                elif board[row][col] in boxes[row//3][col//3]:
                    return False

                rowed.append(board[row][col])
                cols[col].append(board[row][col])
                boxes[row//3][col//3].append(board[row][col])
            
        return True
                