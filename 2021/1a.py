count = 0
with open('1.input') as inputFile:
    input = inputFile.readlines()
    last = int(input[0])
    for depth in input:
        if depth > last:
            count += 1
        last = depth
print(count)
