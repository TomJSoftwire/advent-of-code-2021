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

total_risk = 0

for y in range(0,y_max):
    for x in range(0,x_max):
        val = arr[y][x]
        neigbs = get_neighbours(x,y)

        lower = [x for x in neigbs if arr[x[1]][x[0]] <= val]
        if len(lower) == 0:
            total_risk += 1 + val

print(total_risk)

