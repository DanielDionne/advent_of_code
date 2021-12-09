with open('8.input') as inputFile:
    data = [b.split(' ') for b in [a.rstrip('\n').split(' | ')[1] for a in inputFile.readlines()]]
    result = 0
    for d in data:
        for e in d:
            if len(e) in [2,3,4,7]:
                result += 1
    print(result)
