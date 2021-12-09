from itertools import permutations

def validateNumber(d, p):
    t = []
    for l in d:
        t += chr(p[ord(l)-ord('a')]+(ord('a')))
    t = "".join(sorted(t))
    return t in ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def validate(data, p):
    for d in data:
        if validateNumber(d,p) == False:
            return False
    return True

def findCombination(data):
    for p in list(permutations(range(7), 7)):
        if validate(data, p):
            return p
    return None

def match(matches, digits):
    result = 0
    ten = 1
    for digit in reversed(digits):
        result += ten * matches[digit]
        ten *= 10
    return result

def transform(digit, p):
    t = []
    for l in digit:
        t += chr(p[ord(l)-ord('a')]+(ord('a')))
    t = "".join(sorted(t))
    return {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}[t]

def resolve(digits, p):
    result = 0
    tens = 1
    for digit in reversed(digits):
        result += transform(digit, p) * tens
        tens *= 10
    return result

with open('8.input') as inputFile:
    filedata = inputFile.readlines()
    data = [b.split(' ') for b in [a.rstrip('\n').split(' | ')[0] for a in filedata]]
    digits = [b.split(' ') for b in [a.rstrip('\n').split(' | ')[1] for a in filedata]]
    for d in data:
        for i in range(len(d)):
            d[i] = "".join(sorted(d[i]))
    for d in digits:
        for i in range(len(d)):
            d[i] = "".join(sorted(d[i]))
    total = 0
    for i in range(len(data)):
        p = findCombination(data[i])
        total += resolve(digits[i], p)

    print(total)
