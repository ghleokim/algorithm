from pprint import pprint

graph = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접행렬 이용
N = 7
adj = [[0 for i in range(N)] for j in range(N)]
pprint(adj)

for i in range(len(graph)//2):
    adj[graph[2*i]-1][graph[2*i+1]-1] = 1
    adj[graph[2*i+1]-1][graph[2*i]-1] = 1
pprint(adj)

# 재귀
cur = 0
visited = [0] * N
def DFS(cur, visited):  
    if visited[cur]:
        print()
        visited[cur] = 0
        return 1
    
    visited[cur] = 1
    print(cur+1, end='-')
    
    for idx, num in enumerate(adj[cur]):
        if num:
            if not visited[idx]:
                cur = idx
                DFS(cur, visited)

    return 0
    
DFS(cur, visited)