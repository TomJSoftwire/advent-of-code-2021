import statistics

with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

most = list(input)
least = list(input)

binNumLen = len(input[0])
cur = 0
while (len(most) > 1):
    bits = list(map(lambda x: int(x[cur]), most))
    avgBit = statistics.mean(bits)
    most = list(filter(lambda x: x[cur] == '1' if avgBit >= 0.5 else x[cur] == '0', most))
    cur += 1
    print(most)

cur = 0
while (len(least) > 1):
    bits = list(map(lambda x: int(x[cur]), least))
    avgBit = statistics.mean(bits)
    least = list(filter(lambda x: x[cur] == '1' if avgBit < 0.5 else x[cur] == '0', least))
    cur += 1
    print(least)

numA = int(most[0],2)
numB = int(least[0],2)

print(numA)

print(numB * numA)