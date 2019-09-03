from pprint import pprint

"""direction
0   1   2
3   N   4
5   6   7

"""
di = (-1,-1,-1, 0, 0, 1,  1, 1)
dj = (-1, 0, 1,-1, 1, -1, 0, 1)

def put(j,i,n):
    B[i][j] = n
    queue = [(k,1) for k in range(8)] # k: direction

    cnt = 0
    while queue:
        k, dep = queue[0]
        del queue[0]
        ni,nj = i+di[k]*dep,j+dj[k]*dep
        if any((ni<0, nj<0, ni>N-1, nj>N-1)): continue # boundary
        if B[ni][nj] and B[ni][nj] != n:
            queue.append((k,dep+1))
        elif B[ni][nj] and B[ni][nj] == n:
            cnt += dep-1
            for d in range(1,dep):
                B[i+di[k]*d][j+dj[k]*d] = n
    
    if n % 2:
        result[n] += cnt+1
        result[n+1] -= cnt
        print(n, n+1, cnt, result)
    else:
        result[n] += cnt+1
        result[n-1] -= cnt
        print(n, n-1, cnt, result)

for T in range(int(input())):
    N, M = map(int,input().split())
    B = [[0 for i in range(N)] for j in range(N)]
    result = [0,2,2]
    for i in range(N//2-1, N//2+1):
        for j in range(N//2-1, N//2+1):
            if i == j:
                B[i][j] = 2
            else:
                B[i][j] = 1

    for m in range(M):
        turn = [*map(int,input().split())]
        put(turn[0]-1,turn[1]-1,turn[2])

    print('#',end='')
    print(T+1,result[1],result[2])

"""tc
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2

"""