with open('input.txt') as data:
    input = data.read().split('\n')[:-1]
data = []
signalLens = [6,2,5,5,4,5,6,3,7,6]
uniqueSignalLens = [2,3,4,7]
for line in input:
    splitLine = line.split(' | ')
    tests = splitLine[0].split(' ')
    output = splitLine[1].split(' ')
    data.append([tests, output])

count = 0
for line in data:
    print(line)
    for value in line[1]:
        if len(value) in uniqueSignalLens:
            count += 1
print(count)