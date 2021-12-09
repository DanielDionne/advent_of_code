import re
def addLine(line, board):
    if line[0] == line[2]:
        start = min(line[1], line[3])
        end = max(line[1], line[3]) +1
        for x in range(start, end):
            board[x][line[0]] += 1
    elif line[1] == line[3]:
        start = min(line[0], line[2])
        end = max(line[0], line[2]) +1
        for y in range(start, end):
            board[line[1]][y] += 1
    else:
        if line[0] < line[2]:
            # 0,1 -> 2,3
            for y in range(line[0],line[2]+1):
                if line[1] < line[3]:
                    # goes up
                    x = line[1] + y - line[0]
                    board[x][y] += 1
                else:
                    x = line[1] - (y - line[0])
                    board[x][y] += 1
        else:
            # 2,3 -> 0,1
            for y in range(line[2],line[0]+1):
                if line[3] < line[1]:
                    # goes up
                    x = line[3] + y - line[2]
                    board[x][y] += 1
                else:
                    x = line[3] - (y - line[2])
                    board[x][y] += 1

def countOverlaps(board):
    count = 0
    for row in board:
        for elem in row:
            if elem > 1:
                count += 1
    return count

def solve():
    with open('5.input') as inputFile:
        lines = []
        width = 0
        height = 0
        for lineString in inputFile.readlines():
            # 0,9 -> 5,9
            line = map(int,re.match(r'(\d+),(\d+) -> (\d+),(\d+)', lineString).groups())
            width = max(width, max(line[0], line[2]))
            height = max(height, max(line[1], line[3]))
            lines.append(line)
        width += 1
        height += 1
        board = [[0] * width for i in range(height)]
        for line in lines:
            addLine(line,board)
        print(countOverlaps(board))

solve()
