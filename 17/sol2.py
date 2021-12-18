with open('input.txt') as data:
    input = data.read().split('\n')[:-1]
xTarget = [281,311]
yTarget = [-74, -54]

def getNextPos(pos, vx, vy):
    posN = list(pos)
    posN[0] += vx
    posN[1] += vy

    vyN = vy - 1
    vxN = vx - (1 if vx > 0 else 0)

    return (posN, vxN, vyN)


def getStepsForV(v):
    vx = v[0]
    vy = v[1]
    pos = [0,0]
    steps = []
    while pos[0] <= xTarget[1] and pos[1] >= yTarget[0]:
        steps.append(pos)
        pos, vx, vy = getNextPos(pos, vx, vy)
    return steps

def vHitsTarget(v):
    lastStep = getStepsForV(v)[-1]
    x = lastStep[0]
    y = lastStep[1]
    return x >= xTarget[0] and x <= xTarget[1] and y >= yTarget[0] and y <= yTarget[1]

count = 0 
for vy in range(-abs(yTarget[0]), abs(yTarget[0])):
      for vx in range(0, xTarget[1] + 1):
          if vHitsTarget([vx,vy]):
              count += 1
print(count)
