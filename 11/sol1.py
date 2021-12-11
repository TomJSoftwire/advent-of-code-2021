import time
import sys
import os
import random
with open('input.txt') as data:
    input = data.read().split('\n')[:-1]


octopi = [[int(char) for char in row] for row in input]
def mutate_octopi(fn, octopi):
    octopi = [[fn(char) for char in row] for row in octopi]
    return octopi

def has_10_or_higher(octopi):
    greater_than_10 = mutate_octopi(lambda x: x > 9, octopi)
    return True in [True in row for row in greater_than_10]

def all_flash(octopi):
    is_flash = mutate_octopi(lambda x: x == 0, octopi)
    return not False in [not False in row for row in is_flash]

colors = [
     '\033[95m',
     '\033[94m',
     '\033[96m',
     '\033[92m',
     '\033[93m',
     '\033[91m',
     '\033[1m',
     '\033[4m',]
endCol = '\033[0m'

def getFlash():
    colorInd = random.randrange(len(colors))
    return f'{colors[colorInd]}*{endCol}'

def print_octopi(octopi):
    os.system('clear')
    sys.stdout.write('\n'.join([''.join([' ' if num != 0 else getFlash() for num in row]) for row in octopi]))
    sys.stdout.flush()
flashes = 0
i = 0
while True:
    # print(f'\nstep {i+1}:')
    octopi = mutate_octopi(lambda x: x + 1, octopi)
    while has_10_or_higher(octopi):
        for row in range(0, len(octopi)):
            for col in range(0, len(octopi[0])):
                if octopi[row][col] > 9:
                    flashes += 1
                    for x in range(-1,2):
                        for y in range(-1,2):
                            x_c = row + x
                            y_c = col + y
                            if x_c >= 0 and x_c < len(octopi) and y_c >= 0 and y_c < len(octopi[0]):
                                if octopi[row + x][col + y] != -1:
                                    octopi[row + x][col + y] += 1
                    octopi[row][col] = -1
    octopi = mutate_octopi(lambda x: 0 if x == -1 else x, octopi)
    print_octopi(octopi)
    i += 1
    time.sleep(0.3)
    
# print(flashes)
# print (i)


    
