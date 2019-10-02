


N = int(input())
arr = [*map(int,input().split())]
visited = [0 for _ in range(N+1)]

dist = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+2):
    for j in range(N+2):
        if i == j: continue
        else:
            dij = abs(arr[2*i] - arr[2*j]) + abs(arr[2*i+1] - arr[2*j+1])
            dist[i][j] = dij
            dist[j][i] = dij

from pprint import pprint

pprint(dist)

min_distance = 2000

dfs()

"""4
0 0 100 100 70 40 30 10 10 5 90 70"""