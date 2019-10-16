graph = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

N = len(graph)
adj = [[0] * 8 for i in range(8)]

for k in range(N//2):
    i=graph[k*2]
    j=graph[k*2+1]

    adj[i][j] = adj[j][i] = 1

from pprint import pprint
pprint(adj)

# recursive DFS
def rec_DFS(v):
    visited[v] = 1
    result_dfs.append(v)
    for nv in range(1,N//2):
        if not adj[v][nv]: continue
        elif visited[nv]: continue
        else:
            rec_DFS(nv)

visited = [0 for _ in range(8)]
result_dfs = []
rec_DFS(1)
print(result_dfs)


# repetitive DFS
def rep_DFS(v):
    stack = [0]*8

    top = 0
    stack[top] = v

    while top != -1:
        print('stack', stack)
        cur = stack[top]
        top -= 1
        if not visited[cur]:
            result_dfs2.append(cur)
            visited[cur] = 1
        
        for i in range(1,N//2):
            if not adj[cur][i]: continue
            elif visited[i]: continue
            else:
                top += 1
                stack[top] = i
        

visited = [0 for _ in range(8)]
result_dfs2 = []
rep_DFS(1)
print(result_dfs2)
    

# BFS
def BFS(v):
    queue = [0 for _ in range(10)]
    front = -1
    rear = -1
    rear += 1
    queue[rear] = v
    visited[v] = 1
    result_bfs.append(v)

    while front != rear:
        print('queue', queue)
        front += 1
        cur = queue[front]

        for i in range(1, N//2):
            if not adj[cur][i]: continue
            elif visited[i]: continue
            else:
                result_bfs.append(i)
                visited[i] = 1
                rear += 1
                queue[rear] = i 

visited = [0 for _ in range(8)]
result_bfs = []
BFS(1)
print(result_bfs)