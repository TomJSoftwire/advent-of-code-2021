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

def vyCanHit(vy):
    vx = 0
    while vx <= xTarget[1]:
        if(vHitsTarget([vx,vy])):
            return True, [vx, vy]
        vx += 1
    return False

vy = 0
mvy = 0
while(vy < abs(yTarget[0])):
    vy += 1
    if(vyCanHit(vy)):
        mvy = vy

def get_apex(vy):
    return int(0.5 * vy * (vy + 1))
print(mvy)
print(get_apex(mvy))        

