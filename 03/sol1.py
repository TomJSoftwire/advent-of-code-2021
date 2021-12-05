import statistics

with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

most = ''
least = ''

len = len(input[0])
for i in range(0, len):
    bits = list(map(lambda x: int(x[i]), input))
    avgBit = statistics.mean(bits)
    if(avgBit > 0.5):
        most += '1'
        least += '0'
    else:
        most += '0'
        least += '1'
numA = int(most,2)
numB = int(least,2)

print(numB * numA)