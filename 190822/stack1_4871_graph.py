# swexpertacademy 4871
import sys
sys.stdin = open('input/input4871.txt', 'r')
"""
V E
nodes
S G
"""

# 1 순서 그대로 따라가기
# 1-1 인접행렬
for T in range(int(input())):
    V, E = map(int, input().split())

    board = [[0 for _ in range(V+1)] for __ in range(V+1)]

    for i in range(E):
        vs, vg = map(int, input().split())
        board[vs][vg] = 1

    S, G = map(int, input().split())

    stack = [0] * E
    top = -1
    visited = [0] * (V+1)
    found = 0

    top += 1
    stack[top] = S

    while top != -1:
        # print(stack, top)
        cur = stack[top]
        top -= 1
        if not visited[cur]:
            if cur == G:
               found=1
               break
            visited[cur] = 1
        
            for i in range(1,V+1):
                if board[cur][i] and not visited[i]:
                    top += 1
                    stack[top] = i

    print('#{0} {1}'.format(T+1, found))

# 1-2 인접리스트
# 2 역방향 탐색 + 백트래킹