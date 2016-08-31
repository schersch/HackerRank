def next_move(posx, posy, dimx, dimy, board):
    if(board[posx][posy] =="d"):
        print("CLEAN")
    else:
        dirty = []
        ro = 0
        co = 0
        shortest = 0
        for i in board:
            for j in i:
                if j == "d":
                    dirty.append([ro,co])
                co = co + 1
            co = 0
            ro = ro + 1
        distance = []
        for i in dirty:
            distance.append(abs(i[0]-posx) + abs(i[1]-posy))
        shortest = distance.index(min(distance))
        if dirty[shortest][0] > posx:
            print("DOWN")
        elif dirty[shortest][0] < posx:
            print("UP")
        elif dirty[shortest][1] > posy:
            print("RIGHT")
        else:
            print("LEFT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
