import sys
sys.stdin = open('input/5653.txt', 'r')

def spread(cell):
    cn, cm = cell[0], cell[1]
    energy = board[cn][cm]
    for dn, dm in ((-1,0), (1,0), (0,-1), (0,1)):
        nn, nm = cn + dn, cm + dm
        if board[nn][nm] == 0:
            board[nn][nm] = (energy)
            cleanup.append((nn,nm))
        elif type(board[nn][nm]) == tuple:
            board[nn][nm] = (max(board[nn][nm][0], energy))

for T in range(int(input())):
    N, M, K = map(int,input().split())
 
    board = [ [0 for _ in range(M+K)] for __ in range(N+K) ]
 
    sleeping = []
 
    for i in range(K//2, N+K//2):
        line = [*map(int,input().split())]
        for j in range(K//2, M+K//2):
            board[i][j] = line[j-K//2]
            if line[j-K//2] != 0: sleeping.append([i,j,line[j-K//2],line[j-K//2]])
    
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

        # shortest
        sleeping = [x for x in sleeping if x[3] != 0] + [[tn,tm,board[tn][tm],board[tn][tm]] for tn,tm in cleanup]
        
        # # 풀어쓴 것
        # newsleeping = []
        # for cell in sleeping:
        #     if cell[-1] != 0:
        #         newsleeping.append(cell)
         
        # sleeping = newsleeping

        # # 최대 생명력 반영
        # for tn, tm in cleanup:
        #     sleeping.append([tn,tm,board[tn][tm],board[tn][tm]])
         
    print('#', end='')
    print(T+1,len(sleeping))
