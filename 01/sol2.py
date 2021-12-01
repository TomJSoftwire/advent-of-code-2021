with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

inputInt = list(map(lambda n: int(n), input))
count2 = 0
index = 0
previous = inputInt[index] + inputInt[index + 1] + inputInt[index + 2]
while index < len(input) - 2:
    group = inputInt[index] + inputInt[index + 1] + inputInt[index + 2]
    if group > previous:
        count2+=1
    previous = group
    index += 1

print(count2)