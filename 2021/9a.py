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

with open('9.input') as inputFile:
    rows = [x.strip('\n') for x in inputFile.readlines()]
    lowPoints = []
    height = len(rows)
    for y in range(height):
        row = rows[y]
        width = len(row)
        for x in range(width):
            if isLow(x, y, width, height, rows):
                lowPoints.append(int(rows[y][x]) + 1)
    print(sum(lowPoints))
