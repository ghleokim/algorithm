"""
# array
def bfs(v=1):
    global count
    queue = [(v, 0)]
    
    while queue:
        cur, depth = queue[0]
        del queue[0]

        if depth == 2: continue

        for k in range(2,N+1):
            if k == cur: continue
            elif not adj[cur][k]: continue
            elif visited[k]: continue
            else:
                count += 1
                visited[k] = 1
                queue.append((k, depth+1))

for T in range(int(input())):
    N, M = map(int,input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for _ in range(M):
        i,j = map(int,input().split())
        adj[i][j] = adj[j][i] = 1

    count = 0
    bfs()
    print('#',end='')
    print(T+1,count)
"""


