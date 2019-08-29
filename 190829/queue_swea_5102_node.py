for T in range(int(input())):
    V, E = map(int, input().split())

    # 인접행렬: without 0, indexing 1 ~ N
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # visited
    visited = [0 for _ in range(V+1)]

    # set Queue: max range 2*E
    Q = [0 for _ in range(2*E)]
    front, rear = -1, -1

    S, G = map(int, input().split())
    
    # enQueue
    rear += 1
    Q[rear] = (adj[S], 1)
    visited[S] = 1

    while front != rear:
        # deQueue
        front += 1
        cur, depth = Q[front]
        Q[front] = 0
        found = False
        for c in cur:
            if c == G:
                found = True
                break
            if not visited[c]:
                #enQueue
                visited[c] = 1
                rear += 1
                Q[rear] = (adj[c], depth+1)
        if found:
            break
    # 못찾는 경우
    else:
        depth = 0
    print('#',end='');print(T+1,depth)

 
"""
tc
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

"""