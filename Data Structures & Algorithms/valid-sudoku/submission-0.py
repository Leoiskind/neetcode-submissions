class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(index):
            duplicates = set()
            for i in board[index]:
                if i not in duplicates or i == '.':
                    duplicates.add(i)
                else:
                    return False
            return True

        def checkCol(index):
            duplicates = set()
            for i in range(9):
                num = board[i][index]
                if num not in duplicates or num == '.':
                    duplicates.add(num)
                else:
                    return False
            return True
        
        def checkSquares():
            for squareRow in range(3):
                for squareCol in range(3):
                    duplicates = set()
                    for i in range(3):
                        for j in range(3):
                            num = board[i + squareRow * 3][j + squareCol * 3]
                            if num not in duplicates or num == ".":
                                duplicates.add(num)
                            else:
                                return False
            return True
        
        for i in range(9):
            if not checkRow(i) or not checkCol(i):
                return False

        return checkSquares()