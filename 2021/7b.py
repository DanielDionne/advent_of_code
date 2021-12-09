from collections import Counter
costs = {0:0}

def calculateCost(n):
    if n in costs:
        return costs[n]
    return costs.setdefault(n, calculateCost(n-1)+n)

def calculateCosts(target, inputCounts):
    result = 0
    for value,num in inputCounts:
        result += calculateCost(abs(target-value)) * num
    return result

with open('7.input') as inputFile:
    input = sorted(map(int,inputFile.readlines()[0].split(',')))
    bestCost = float('inf')
    inputCounts = Counter(input).items()
    for i in range(max(input)):
        cost = calculateCosts(i, inputCounts)
        bestCost = min(cost,bestCost)
    print(bestCost)
