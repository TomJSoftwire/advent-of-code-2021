with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

# print(input)

def is_corrupt(line):
    open = ['(', '{' ,'[', '<']
    close = [')', '}' ,']', '>']
    nextClose = [None]
    for char in list(line):

        if char in close:
            if char == nextClose[0]:
                nextClose.pop(0)
            else:
                return True, char
        elif char in open:
            ind = open.index(char)
            nextClose.insert(0,close[ind])
    
    return False, ''
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
count = 0
for line in input:
    is_broken, breaking_char = is_corrupt(line)
    if is_broken:
        count += points[breaking_char]

print(count)
