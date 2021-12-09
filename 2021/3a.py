width=12
s = [0]*width
with open('3.input') as inputFile:
    for line in inputFile.readlines():
        for i in range(width):
            if line[i] == '1':
                s[i] += 1
            else:
                s[i] -= 1
gamma = 0
epsilon = 0
b = 1
for i in reversed(s):
    if i > 0:
        gamma += b
    else:
        epsilon += b
    b = b*2

result = gamma * epsilon
print(result)
