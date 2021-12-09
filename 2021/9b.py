import operator
def isLow(x, y, w, h, rows):
    p = rows[y][x]
    # up
    if y > 0 and p >= rows[y-1][x]:
        return False
    # down
    if y < h-1 and p >= rows[y+1][x]:
        return False
    # left
    if x > 0 and p >= rows[y][x-1]:
        return False
    # right
    if x < w-1 and p >= rows[y][x+1]:
        return False
    return True

def getBasinSize(x, y, w, h, rows, visited):
    if (x,y) in visited:
        return 0
    if x < 0 or x >= w or y < 0 or y >= h or rows[y][x] == '9':
        return 0
    visited.add((x,y))
    result = 1
    for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_x = x + dir[0]
        next_y = y + dir[1]
        result += getBasinSize(next_x, next_y, w, h, rows, visited)
    return result

with open('9.input') as inputFile:
    rows = [x.strip('\n') for x in inputFile.readlines()]
    lowPoints = []
    height = len(rows)
    width = len(rows[0])
    for y in range(height):
        row = rows[y]
        for x in range(width):
            if isLow(x, y, width, height, rows):
                lowPoints.append((x,y))
    basins = []
    for lowPoint in lowPoints:
        visited = set()
        basins.append(getBasinSize(lowPoint[0], lowPoint[1], width, height, rows, visited))
    threeLargest = sorted(basins, reverse = True)[:3]
    print(reduce(operator.mul, threeLargest, 1))
