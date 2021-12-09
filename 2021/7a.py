from collections import Counter
with open('7.input') as inputFile:
    input = sorted(map(int,inputFile.readlines()[0].split(',')))
    rightCost = sum(input)
    rightCount = len(input)
    leftCost = 0
    leftCount = 0
    bestCost = rightCost
    solution = 0
    inputCounts = Counter(input).items()
    for i in range(len(inputCounts)):
        value,num = inputCounts[i]
        if i==0:
            total = rightCost
            leftCount += num
            rightCount -= num
        else:
            distance = value - inputCounts[i-1][0]
            rightCost -= rightCount * distance
            rightCount -= num
            leftCost += leftCount * distance
            leftCount += num
            total = leftCost + rightCost

        print("Cost at %i is %i"%(value, total))
        if total < bestCost:
            bestCost = total
            solution = value
    print(solution, bestCost)
