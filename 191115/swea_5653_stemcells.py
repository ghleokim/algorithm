import sys
sys.stdin = open('input/5653.txt', 'r')

def spread(cell):
    cn, cm = cell[0], cell[1]
    energy = board[cn][cm]
    for dn, dm in ((-1,0), (1,0), (0,-1), (0,1)):
        nn, nm = cn + dn, cm + dm
        if board[nn][nm] == 0:
            board[nn][nm] = [energy]
            cleanup.append((nn,nm))
        elif type(board[nn][nm]) == list:
            board[nn][nm].append(energy)

for T in range(int(input())):
    N, M, K = map(int,input().split())

    board = [ [0 for _ in range(M + K*2)] for __ in range(N + K*2) ]

    sleeping = []

    for i in range(K, K+N):
        line = [*map(int,input().split())]
        for j in range(K, K+M):
            board[i][j] = line[j-K]
            if line[j-K] != 0: sleeping.append([i,j,line[j-K],line[j-K]])

    t = 0

    while t < K:
        cleanup = []
        t+= 1
        for cell in sleeping:
            if cell[2] != 0:
                # not awake
                cell[2] -= 1
            elif cell[3] != 0:
                # alive
                cell[3] -= 1
                spread(cell)

        # 최대 생명력 반영
        for tn, tm in cleanup:
            val = max(board[tn][tm])
            board[tn][tm] = val
            sleeping.append([tn,tm,val,val])

        newsleeping = []
        for cell in sleeping:
            if cell[2] != 0 or cell[3] != 0:
                newsleeping.append(cell)
        
        sleeping = newsleeping
    print('#', end='')
    print(T+1,len(sleeping))