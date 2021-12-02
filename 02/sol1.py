with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

x = 0
y = 0

for i in input:
    inst = str.split(i, ' ')
    dir = inst[0]
    mag = int(inst[1])
    if dir == 'forward':
        x += mag
    if dir == 'down':
        y += mag
    if dir == 'up':
        y -= mag

print(x * y)