import re

def mark(number, board):
    for row in board:
        for element in row:
            if element[0] == number:
                element[1] = True

def check(board):
    # check rows
    for row in board:
        if all([e[1] == True for e in row]):
            return True
    # check columns
    for colIndex in range(len(board)):
        if all([board[rowIndex][colIndex][1] for rowIndex in range(len(board))]):
            return True
    return False

def sumUnmarked(board):
    return sum([e[0],0][e[1]] for row in board for e in row)

def solve():
    with open('4.input') as inputFile:
        lines = inputFile.readlines()
        numbers = map(int, lines[0].split(','))

        boards = []
        boardLines = []
        for line in lines[2:]:
            if len(line) == 1:
                boards += [boardLines]
                boardLines = []
                continue
            lineNumbers = [[x,False] for x in map(int,[line[0:2], line[3:5], line[6:8], line[9:11], line[12:14]])]
            boardLines += [lineNumbers]
        boards += [boardLines]

        for number in numbers:
            for board in boards:
                mark(number, board)
                if check(board):
                    # calculate result
                    # sum of all unmarked numbers
                    s = sumUnmarked(board)
                    # multiply that sum by the number that was just called
                    print(s*number)
                    return
solve()
