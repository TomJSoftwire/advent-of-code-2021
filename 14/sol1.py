with open('input.txt') as data:
    input = data.read().split('\n')

template, rules = input[0], {pair:insert for (pair, insert) in (r.split(' -> ') for r in input[2:])}

pairCountsTemp = {pair: 0 for pair in rules.keys() }
pairCounts = dict(pairCountsTemp)

for i in range(0,len(template)-1):
    pair = template[i: i + 2]
    pairCounts[pair] += 1

for j in range(0,40):
    newPairCount = dict(pairCountsTemp)
    for pair in pairCounts.keys():
        insert = rules[pair]
        newPairCount[pair[0] + insert] += pairCounts[pair]
        newPairCount[insert + pair[1]] += pairCounts[pair]
    pairCounts = newPairCount
    
letterCounts = {}
for pair in pairCounts.keys():
    for letter in [pair[0], pair[1]]:
        if letter in letterCounts.keys():
            letterCounts[letter] += pairCounts[pair]
        else:
            letterCounts[letter] = pairCounts[pair]

letterCounts[template[0]] += 1
letterCounts[template[-1]] += 1

invertedCount = {value:key for (key,value) in letterCounts.items()}

high = max(invertedCount.keys())
low = min(invertedCount.keys())

print(int((high-low)/2))