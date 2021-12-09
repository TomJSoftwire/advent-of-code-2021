with open('input.txt') as data:
    input = data.read().split('\n')

arr = [[int(char) for char in row] for row in input]
x_max = len(arr[0])
y_max = len(arr)

def get_neighbours(x,y):
    neighbs = []
    for xT in range(-1, 2):
        for yT in range(-1,2):
            xN = x + xT
            yN = y + yT
            if (xT == 0 and yT !=0) or (yT == 0 and xT != 0):
                if xN >= 0 and xN < x_max and yN >= 0 and yN < y_max:
                    neighbs.append([xN,yN])
    return neighbs

basins = []

for y in range(0,y_max):
    for x in range(0,x_max):
        val = arr[y][x]
        neigbs = get_neighbours(x,y)

        lower = [x for x in neigbs if arr[x[1]][x[0]] <= val]
        if len(lower) == 0:
            basins.append([f'{x},{y}'])

def getHigherNebs(point):
    x = point[0]
    y = point[1]
    nebs = get_neighbours(x,y)
    val = arr[y][x]
    # print(val)
    # print(nebs)
    higher = [f'{x[0]},{x[1]}' for x in nebs if (arr[x[1]][x[0]] > val and arr[x[1]][x[0]] != 9)]
    return set(higher)

def getBasin(lowPoints):
    finalPoints = set()
    newPoints = set(lowPoints)
    while len(newPoints) != len(finalPoints):
        finalPoints = set(newPoints)
        for point in newPoints:
            newPoints = newPoints.union(getHigherNebs([int(x) for x in point.split(',')]))

    return finalPoints
fullBasins = []
for low in basins:
    start =  set(low)
    basin = getBasin(start)
    fullBasins.append(len(basin))

print(fullBasins)
print(fullBasins.sort())
print(fullBasins[-3] * fullBasins[-2] * fullBasins[-1])

