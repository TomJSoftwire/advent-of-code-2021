with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

x = 0
y = 0
a = 0

for i in input:
    inst = str.split(i, ' ')
    dir = inst[0]
    mag = int(inst[1])
    if dir == 'forward':
        x += mag
        y += mag * a
    if dir == 'down':
        a += mag
    if dir == 'up':
        a -= mag

print(x * y)