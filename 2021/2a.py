pos = [0,0]
with open('2.input') as inputFile:
    for line in inputFile.readlines():
        direction,amount = line.split(' ')
        if direction == 'forward':
            pos[0] += int(amount)
        elif direction == 'down':
            pos[1] += int(amount)
        else:
            pos[1] -= int(amount)
print(pos[0] * pos[1])
