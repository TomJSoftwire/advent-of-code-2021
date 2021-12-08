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
    disp = [None,None,None,None,None,None,None,None,None,None]
    missingValByLen = [[],[],[],[],[],[],[],[],[],[]]
    segmentDict = {}
    for value in line[0]:
        signalLen = len(value)
        if signalLen in uniqueSignalLens:
            num = signalLens.index(signalLen)
            disp[num] = set(value)
        else:
            missingValByLen[signalLen].append(set(value))

    # Get 6
    for value in missingValByLen[6]:
        if len(disp[1].intersection(value)) == 1:
            disp[6] = value
            missingValByLen[6].remove(value)
    
    # Get 5
    for value in missingValByLen[5]:
        if len(disp[6].intersection(value)) == 5:
            disp[5] = value
            missingValByLen[5].remove(value)
    
    # Get e
    segmentDict['e'] = list(disp[6].difference(disp[5]))[0]

    # Get 9 and 0
    for value in missingValByLen[6]:
        if segmentDict['e'] in value:
            disp[0] = value
        else:
            disp[9] = value
    
    # Get 2 and 3
    for value in missingValByLen[5]:
        if segmentDict['e'] in value:
            disp[2] = value
        else:
            disp[3] = value

    outputNum = ''

    for output in line[1]:
        num = disp.index(set(output))
        outputNum += str(num)

    count += int(outputNum)

print(count)