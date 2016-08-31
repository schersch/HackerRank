#Bot Saves Princess 2

def nextMove(n,r,c,grid):
    pPos = []
    pPos.append(0)
    bPos = []
    bPos.append(0)
    
    for i in grid:
        try:
            pPos.append(i.index('p'))
            break
        except:
            pPos[0] = pPos[0]+1
            pass
    if len(pPos)<2:
        return
    
    for j in grid:
        try:
            bPos.append(j.index('m'))
            break
        except:
            bPos[0]=bPos[0]+1
            pass
    if bPos[0] > pPos[0]:
        return("UP")
    elif bPos[0] < pPos[0]:
        return("DOWN")
    elif bPos[1] < pPos[1]:
        return("RIGHT")
    elif bPos[1] > pPos[1]:
        return("LEFT")
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
