scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def findFirstCorrupted(line):
    stack = []
    for symbol in line:
        if symbol in ['(', '[', '{' ,'<']:
            stack.append(symbol)
        else:
            for p in [('(',')'), ('[',']'), ('{','}'), ('<','>')]:
                if symbol == p[1]:
                    if stack[-1] == p[0]:
                        stack.pop()
                        break
                    else:
                        return symbol


with open('10.input') as inputFile:
    score = 0
    lines = inputFile.readlines()
    for line in lines:
        s = findFirstCorrupted(line)
        if s:
            score += scores[s]
    print(score)
