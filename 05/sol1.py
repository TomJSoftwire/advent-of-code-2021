with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

lines = []

for line in input:
    pointsRaw = line.split(' -> ')
    points = [pointsRaw[0].split(','),pointsRaw[1].split(',')]
    lines.append(points)

rowTemplate = []
grid =[]

for line in lines:
    x1 = int(line[0][0])
    x2 = int(line[1][0])
    y1 = int(line[0][1])
    y2 = int(line[1][1])
    rowPos = max([x1, x2])
    colPos = max([y1, y2])
    
    while len(rowTemplate) <= rowPos:
        rowTemplate.append(0)
        for row in grid:
            row.append(0)
    while len(grid) <= colPos:
        grid.append(list(rowTemplate))
    
    if (x1 == x2):
        ye = max([y1,y2])
        ys = min([y1,y2])
        for y in range(ys, ye + 1):
            grid[y][x1] += 1
    elif (y1 == y2):
        xe = max([x1,x2])
        xs = min([x1,x2])
        for x in range(xs,xe + 1):
            grid[y1][x] += 1
    else:
        dx = x2 - x1
        x = x2 if dx < 0 else x1
        ys = y2 if dx < 0 else y1
        ye = y1 if dx < 0 else y2
        dy = ye - ys
        y = ys
        while x <= max([x1,x2]):
            grid[y][x] += 1
            x += 1
            y += -1 if dy < 0 else 1
            
count = 0
for line in grid:
    for entry in line:
        if entry > 1:
            count += 1

print(count)
