# Prim algorithm

def extract_min(queue):
    min_key = 1000
    min_i = -1
    for q in queue:
        if key[q] < min_key:
            min_key = key[q]
            min_i = q
    del queue[queue.index(min_i)]

    return min_i

for T in range(int(input())):
    V, E = map(int,input().split())
    queue = [i for i in range(V+1)]
    key = [1000 for i in range(V+1)]

    adj = [[0 for _ in range(V+1)] for __ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int,input().split())
        adj[n1][n2] = adj[n2][n1] = w

    key[0] = 0

    while queue:
        u = extract_min(queue)
        # print(u, queue)

        for i in range(V+1):
            if i not in queue: continue
            elif not adj[u][i]: continue
            elif key[i] < adj[u][i]: continue
            else:
                key[i] = adj[u][i]

    print(T+1, sum(key))
