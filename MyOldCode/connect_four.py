def create_board(boardDict):
    '''create_board(boardDict) -> string
    prints a Connect Four board using boardDict
    boardDict: dictionary'''
    topRow = '\n'
    board = ''
    # creates column numbers
    for column in range(7):
        topRow += str(column) + ' '
    # creates 6 rows with 7 dots each
    for rowDict in boardDict.values():
        for value in rowDict.values():
            board += value + ' '
        board += '\n'
    print(topRow)
    print(board)

def take_turn(checker,column,boardDict):
    '''take_turn(checker,column,boardDict) -> string
    inserts a checker into a Connect Four board
    checker: string, column: int, boardDict: dictionary'''
    row = 5 # starts from bottom row
    while True:
        # checks if intersection of column and row is filled with checker
        rowDict = boardDict[row]
        # inserts checker if space not filled
        if rowDict[column] == '.':
            rowDict[column] = checker
            break
        # checks above row if space is filled
        else:
            row -= 1
            # asks for different column if column is full
            if row < 0:
                column = int(input('This column is full. Please pick a different column: '))
                row = 5
            # asks for different column if column is not valid
            while column < 0 or column > 6:
                column = int(input('This is not a valid column. Please pick a different column: '))
    board = create_board(boardDict) # prints board with checker inserted in chosen column


def connect_four():
    '''connect_four() -> string
    plays a game of Connect Four'''
    # asks players to input names
    X = input('Player X, enter your name: ')
    O = input('Player O, enter your name: ')

    # creates initial Connect Four board
    boardDict = {}
    row = 0
    for r in range(6):
        rowDict = {} # creates a dictionary for each row
        column = 0
        for c in range(7):
            rowDict[column] = '.' # creates dots corresponding to the intersections of columns with a row
            column += 1
        boardDict[row] = rowDict # stores all row dictionaries in a board dictionary
        row += 1
    board = create_board(boardDict) # prints initial board

    # lists of winning row dictionaries, winning horizontal lines, and winning vertical and diagonal lines
    winningRowDicts = [[0,1,2,3],[1,2,3,4],[2,3,4,5]] 
    winningHs = [[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    winningVsandDs = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6],[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,2,1,0],[4,3,2,1],[5,4,3,2]]
    move = 0
    winner = False
    
    while not winner:
        # turns alternate between player X and player O
        if move % 2 == 0:
            playerName = X
            checker = 'X'
        else:
            playerName = O
            checker = 'O'
        column = int(input(str(playerName) + ", you're " + checker + '. What column do you want to play in? ')) # asks for column to play in
        # asks for different column if column is not valid
        while column < 0 or column > 6:
            column = int(input('This is not a valid column. Please pick a different column: '))
        board = take_turn(checker,column,boardDict) # prints board with checker inserted in chosen column
        # checks each row for a winning horizonal line
        for rowDict in boardDict.values():
            for line in winningHs:
                if rowDict[line[0]] == rowDict[line[1]] == rowDict[line[2]] == rowDict[line[3]] and rowDict[line[0]] in ['X','O']:
                    return 'Congratulations ' + str(playerName) + '! You won!'
                    winner = True # ends game if winner is found
        # checks winning lists of rows for a winning vertical or diagonal line
        for rowDicts in winningRowDicts:
            for line in winningVsandDs:
                if (boardDict[rowDicts[0]])[line[0]] == (boardDict[rowDicts[1]])[line[1]] == (boardDict[rowDicts[2]])[line[2]] == (boardDict[rowDicts[3]])[line[3]] and (boardDict[rowDicts[0]])[line[0]] in ['X','O']:
                    return 'Congratulations ' + str(playerName) + '! You won!'
                    winner = True # ends game if winner is found
        # ends game in tie if board is filled
        if move == 41:
            return 'The game ended in a draw!'
            break
        move += 1

print(connect_four())
