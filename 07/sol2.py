with open('input.txt') as data:
    inputCrab = list(map(lambda x: int(x), data.read().split(',')))

def findMinFuel(input):
    minFuel = 9999999999999
    for pos in range(0,max(input) + 1):
        fuel = 0 
        for crab in input:
            dist = abs(crab - pos)
            fuel += int(0.5 * dist * (dist + 1))
        if fuel < minFuel:
            minFuel = fuel

    print(minFuel)         

findMinFuel(inputCrab)