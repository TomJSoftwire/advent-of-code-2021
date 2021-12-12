with open('input.txt') as data:
    input = data.read().split('\n')[:-1]

class Cave:
    def __init__(self, name):
        self.name = name
        self.isBig = str.upper(name) == name
        self.connections: set[Cave] = set()

# cave = Cave('A')
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
def print_route(route):
    pr = (',').join([c.name for c in route])
    print(pr)

def find_end(route):
    latestCave: Cave = route[-1]
    for nb in latestCave.connections:
        if nb.name == 'end':
            finalRoute = route + [nb]
            routes.add((',').join([c.name for c in finalRoute]))
        elif nb.isBig or not (nb in route):
            # print(f'{nb.name}: {nb in route}')
            updatedRoute = route + [nb]
            # print_route(updatedRoute)
            find_end(updatedRoute)
find_end([start])
# print(routes)
print(len(routes))


