scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def getStack(line):
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
                        return None
    mirror = {'(':')', '[':']', '{':'}', '<':'>'}
    return [mirror[x] for x in reversed(stack)]

def calculateScore(s):
    result = 0
    for symbol in s:
        result = result*5 + scores[symbol]
    return result

with open('10.input') as inputFile:
    score = 0
    lines = inputFile.readlines()
    result = []
    for line in lines:
        s = getStack(line)
        if s:
            result.append(calculateScore(s))
    print(sorted(result)[len(result)/2])
