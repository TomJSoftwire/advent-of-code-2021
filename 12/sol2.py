with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

class Cave:
    def __init__(self, name):
        self.name = name
        self.isBig = str.upper(name) == name
        self.connections: set[Cave] = set()

caveNames = set()
for cx in input:
    cs = cx.split('-')
    caveNames.add(cs[0])
    caveNames.add(cs[1])
caves = {}
for caveName in caveNames:
    caves[caveName] = Cave(caveName)

for connection in input:
    a, b = connection.split('-')
    caves[a].connections.add(caves[b])
    caves[b].connections.add(caves[a])

routes = set()

start: Cave = caves['start']

def find_end_with_small(route, small):
    latestCave: Cave = route[-1]
    def activeDoubleCave(n):
        return n == small and len([c for c in route if c == small]) < 2
    for nb in latestCave.connections:
        if nb.name == 'end':
            finalRoute = route + [nb]
            routes.add((',').join([c.name for c in finalRoute]))
        elif nb.isBig or not (nb in route) or activeDoubleCave(nb):
            updatedRoute = route + [nb]
            find_end_with_small(updatedRoute, small)

smallCaves = [caves[c] for c in caves if not caves[c].isBig and caves[c].name not in ['start', 'end']]
for small in smallCaves:
    find_end_with_small([start], small )

print(len(routes))


