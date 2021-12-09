count = 0
with open('1.input') as inputFile:
    input = inputFile.readlines()
    window = [int(input[0]), int(input[1]), int(input[2])]
    windowDepth = int(input[0]) + int(input[1]) + int(input[2])
    index = 0
    for depth in input[3:]:
        newWindowDepth = windowDepth - window[index%3] + int(depth)
        window[index%3] = int(depth)
        if newWindowDepth > windowDepth:
            count += 1
        windowDepth = newWindowDepth
        last = depth
        index += 1
print(count)
