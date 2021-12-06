with open('input.txt') as data:
    input = list(map(lambda num: int(num), data.read().split(',')))

print(len(input))
print(input)

for day in range(0,80):
    print(f'day {day}')
    for i in range(0, len(input)):
        fish = input[i]
        if fish == 0:
            input.append(8)
            input[i] = 6
        else:
            input[i] -= 1

print(len(input))
    
