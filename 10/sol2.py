import statistics
with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def get_closing_chars(string):
    open = ['(', '{' ,'[', '<']
    close = [')', '}' ,']', '>']
    nextClose = []
    for char in list(line):
        if char in close:
            nextClose.pop(0)
        elif char in open:
            ind = open.index(char)
            nextClose.insert(0,close[ind])
    return nextClose

linePoints = []
for line in input:
    is_broken, breaking_char = is_corrupt(line)
    if not is_broken:
        print(get_closing_chars(line))
        score = 0
        for char in get_closing_chars(line):
            score *= 5
            score += points[char]
        linePoints.append(score)
        

print(statistics.median(linePoints))
