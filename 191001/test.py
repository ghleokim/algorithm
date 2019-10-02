def dfs(k=0):
    if k == N:
        print(visited)
    else:
        for i in range(N):
            if visited[i]: continue
            visited[i] = k+1
            dfs(k+1)
            visited[i] = 0

N = int(input())
visited = [0] * N
dfs()