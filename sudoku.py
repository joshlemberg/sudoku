def isValidSudoku(board):
        for i in range(0,9):
            if any(board[i].count(str(x)) > 1 for x in range(1,10)):
                return False
                
        for i in range(0,9):
            newlist = list(board[x][i] for x in range(0,9))
            if any(newlist.count(str(x)) > 1 for x in range(1,10)):
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                boxlist = board[j][i:i+3] + board[j+1][i:i+3] + board[j + 2][i:i+3]
                if any(boxlist.count(str(x)) > 1 for x in range(1,10)):
                    return False
                
        return True

def PrintSudoku(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print("")

def SudokuSolver(board):
    oldboard = board
##    print("\n\n\nNew Call:")
    if isValidSudoku(board) and not any('.' in sublist for sublist in board):
        print("Returning true on initial condition")
        PrintSudoku(board)
        return [True, board]

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for k in range(1,10):
##                    print("Now setting space ", i, j, "to", k )
                    board[i][j] = str(k)
##                    PrintSudoku(board)
                    if isValidSudoku(board):
                        if SudokuSolver(board)[0]:
                            return [True, board]
                    board[i][j] = '.'
                return [False, board]
    return [False, board]


def SudokuDriver():
    board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    board2 = [[".",".",".","2","6",".","7",".","1"],["6","8",".",".","7",".",".","9","."],["1","9",".",".",".","4","5",".","."],["8","2",".","1",".",".",".","4","."],[".",".","4","6",".","2","9",".","."],[".","5",".",".",".","3",".","2","8"],[".",".","9","3",".",".",".","7","4"],[".","4",".",".","5",".",".","3","6"],["7",".","3",".","1","8",".",".","."]]
##    PrintSudoku(board2)
    SudokuSolver(board1)
    SudokuSolver(board2)

    x = input("Would you like to enter a sudoku board? [y/n]\n")
    if x == 'y':
        boardinput = input("Enter the numbers, left to right, top to bottom, with no space, using . for empty cells\n")
        i = 0
        split_strings = [0 for x in range(9)]
        for c in range(0, 81, 9):
            newstring = boardinput[c : c + 9]
            colarray = [newstring[x] for x in range(9)]
            split_strings[i] = colarray
            i += 1
        SudokuSolver(split_strings)
    else:
        pass
            
