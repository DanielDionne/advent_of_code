days = 80
with open('6.input') as inputFile:
    fish = map(int,inputFile.readlines()[0].split(','))
    for day in range(days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
    print(len(fish))
