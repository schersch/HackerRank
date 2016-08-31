def next_move(posr, posc, board):
    if(board[posr][posc] =="d"):
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
            distance.append(abs(i[0]-posr) + abs(i[1]-posc))
        shortest = distance.index(min(distance))
        if dirty[shortest][0] > posr:
            print("DOWN")
        elif dirty[shortest][0] < posr:
            print("UP")
        elif dirty[shortest][1] > posc:
            print("RIGHT")
        else:
            print("LEFT")
            
            
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
