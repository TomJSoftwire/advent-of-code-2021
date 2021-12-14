with open('input.txt') as data:
    dots, folds = [line.split('\n') for line in data.read().split('\n\n')]

sheet = []
rowTemp = []

def p_sheet(sh):
    re = '\n'.join([' '.join([str(x) for x in r]) for r in sh])
    print(re)

for point in dots:
    row, col = [int(x) for x in point.split(',')]
    while(col >= len(sheet)):
        sheet.append(list(rowTemp))
    while(row >= len(rowTemp)):
        rowTemp.append('.')
        for sheetRow in sheet:
            sheetRow.append('.')
for point in dots:
    # print(point)
    row, col = [int(x) for x in point.split(',')]
    sheet[col][row] = '#'
    # p_sheet(sheet)


    
# p_sheet(sheet)
# print(folds)

def performFold(fold, foldee):
    dir, coord = [fold.split('=')[0][-1], int(fold.split('=')[1][0:])]
    # print(dir)
    # print(coord)
    if(dir == 'y'):
        keep = foldee[0:coord]
        toFold = foldee[coord+1:]
        # p_sheet(toFold)
        # print('----')
        # p_sheet(folded)
        folded = list(reversed(toFold))
    else:
        print(coord)
        keep = [row[0:coord] for row in foldee]
        toFold = [row[coord + 1:] for row in foldee]
        folded = [list(reversed(row)) for row in toFold]
    print('-----')
    print(f'keep: {len(keep[0])}, {len(keep)}')
    # p_sheet(keep)
    print('-----')
    print(f'toFold: {len(toFold[0])}, {len(toFold)}')
    # p_sheet(toFold)
    for x in range(0,len(keep[0])):
        for y in range(0, len(keep)):
            if folded[y][x] == '#':
                # print(f'{x},{y}')
                keep[y][x] = '#'
    return keep

oneFold = performFold(folds[0],sheet)
print('-----')
# p_sheet(oneFold)
# twoFolds = performFold(folds[1],oneFold)
count = 0
for row in oneFold:
    for point in row:
        if point == '#':
            count += 1

# print('-----')
# p_sheet(twoFolds)
print(count)
