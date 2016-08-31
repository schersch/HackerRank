#Bot saves princess

#!/usr/bin/python
def displayPathtoPrincess(n,grid):
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
    #print(grid)
    #print(bPos)
    #print(pPos)
    if bPos[0] > pPos[0]:
        print("UP")
        grid[bPos[0]] = list(grid[bPos[0]])
        grid[bPos[0]][bPos[1]] = "-"
        grid[bPos[0]] = "".join(grid[bPos[0]])
        grid[bPos[0]-1] = list(grid[bPos[0]-1])
        grid[bPos[0]-1][bPos[1]] = "m"
        grid[bPos[0]-1] = "".join(grid[bPos[0]-1])
        #print(grid)
        displayPathtoPrincess(n,grid)
    elif bPos[0] < pPos[0]:
        print("DOWN")
        grid[bPos[0]] = list(grid[bPos[0]])
        grid[bPos[0]][bPos[1]] = "-"
        grid[bPos[0]] = "".join(grid[bPos[0]])
        grid[bPos[0]+1] = list(grid[bPos[0]+1])
        grid[bPos[0]+1][bPos[1]] = "m"
        grid[bPos[0]+1] = "".join(grid[bPos[0]+1])
        #print(grid)
        displayPathtoPrincess(n,grid)
    elif bPos[1] < pPos[1]:
        print("RIGHT")
        grid[bPos[0]] = list(grid[bPos[0]])
        grid[bPos[0]][bPos[1]] = "-"
        grid[bPos[0]] = "".join(grid[bPos[0]])
        grid[bPos[0]] = list(grid[bPos[0]])
        grid[bPos[0]][bPos[1]+1] = "m"
        grid[bPos[0]] = "".join(grid[bPos[0]])
        displayPathtoPrincess(n,grid)
    elif bPos[1] > pPos[1]:
        print("LEFT")
        grid[bPos[0]] = list(grid[bPos[0]])
        grid[bPos[0]][bPos[1]] = "-"
        grid[bPos[0]] = "".join(grid[bPos[0]])
        grid[bPos[0]] = list(grid[bPos[0]])
        grid[bPos[0]][bPos[1]-1] = "m"
        grid[bPos[0]] = "".join(grid[bPos[0]])
        displayPathtoPrincess(n,grid)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
