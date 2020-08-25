"""
BFS. 인접한 노드를 방문하면서 임계 값보다 작아지는 지점을 포착한다.

"""

t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    arr = [[0 for __ in range(n+1)] for ___ in range(n+1)]

    for __ in range(n-1):
        i, j, w = map(int, input().split())
        arr[i][j] = arr[j][i] = w

    queue = [(1, 0, [1])]
    visited = [0 for __ in range(n+1)]
    leaves = []
    leaves_id = []

    while queue:
        cur, cur_w, path = queue[0]
        del queue[0]
        visited[cur] = 1
        leaf = True

        for next_v in range(n+1):
            if arr[cur][next_v] == 0: continue
            elif visited[next_v] == 1: continue
            else:
                leaf = False
                next_w = cur_w + arr[cur][next_v]
                next_p = (*path, next_v)
                queue.append((next_v, next_w, next_p))
        
        if leaf:
            leaves_id.append(cur)
            leaves.append([cur_w, path])

    queue = [(1, 0)] # v, move, max_s

    while queue:
        cur_v, cur_move, cur_s = queue[0]
        del queue[0]

        

        for next_v in range(n+1):
            if arr[cur_v][next_v] == 0: continue
            else:
                diff = arr[cur_v][next_v] - (arr[cur_v][next_v] // 2)

                next_pack = [next_v, cur_move + 1]
                queue.append(next_pack)
