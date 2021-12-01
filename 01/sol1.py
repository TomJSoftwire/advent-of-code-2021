with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

count = 0
previous = int(input[0])
for reading in input:
    if int(reading) > previous:
        count += 1
    previous = int(reading)

print(count)