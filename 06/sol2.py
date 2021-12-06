with open('input.txt') as data:
    input = list(map(lambda num: int(num), data.read().split(',')))

print(len(input))
# print(input)

counts = [0,0,0,0,0,0,0,0,0]
for fish in input:
    counts[fish] += 1

for day in range(0,256):
    newFish = counts[0]
    counts = counts[1:7] + [counts[0] + counts[7]] + [counts[8]] + [counts[0]]
    print(counts)

total = 0

for c in counts:
    total += c
print(counts)
print(total)
    
  