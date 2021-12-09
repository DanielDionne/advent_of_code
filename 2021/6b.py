days = 256

def calculate(f, day, data):
    if day == 0:
        return 1
    if (f,day) in data:
        return data[(f,day)]
    if f > 0:
        result = calculate(f-1, day-1, data)
    else:
        result = calculate(8, day-1, data) + calculate(6, day-1, data)
    data[(f,day)] = result
    return result

with open('6.input') as inputFile:
    fish = map(int,inputFile.readlines()[0].split(','))
    data = {}
    total = 0
    for f in fish:
        total += calculate(f, days, data)
    print (total)
