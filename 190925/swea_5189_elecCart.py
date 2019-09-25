def findpath(depth=1, localsum=0):
    global minsum
    if depth == N:
        print(visited, path, localsum)
        print(path[depth-1], localsum + P[path[depth-1]][0])
        localsum += P[path[depth-1]][0]
        if localsum < minsum:
            minsum = localsum
        return
    elif localsum > minsum:
        print('   skip:::', visited)
        return
    for i in range(N):
        if visited[i] is not None: continue
        visited[i] = 1
        path[depth] = i
        findpath(depth+1, localsum + P[path[depth-1]][i])
        visited[i] = None


for T in range(int(input())):
    N = int(input())
    P = [ [*map(int, input().split())] for __ in range(N) ]
    visited = [None for _ in range(N)]
    visited[0] = 1
    path = [None for _ in range(N)]
    path[0] = 0
    minsum = 100000
    findpath()
    print('#', end='')
    print(T+1,minsum)
