# solvingclub 0822
import sys
sys.stdin = open('input/input190822.txt', 'r')
"""
작업순서가 있는 그래프/ 방향성이 있고 사이클이 없는 그래프

"""
"""
# 순방향 탐색
for T in range(10):
    V, E = map(int, input().split())

    ins = [0 for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    graph = [[] for _ in range(V+1)]

    edges = [*map(int, input().split())]

    for e in range(E):
        graph[edges[2*e]].append(edges[2*e+1])
        ins[edges[2*e+1]] += 1

    stack = [0 for _ in range(V)]
    top = -1
    
    while top < V-1:
        for idx, incount in enumerate(ins[1:]):
            # 진입차수 0인 노드 기준으로 탐색
            if not incount:
                # incount = -1로 설정
                ins[idx+1] -= 1
                if visited[idx+1]:
                    continue
                visited[idx+1] = 1

                # 인덱스 저장
                top += 1
                stack[top] = idx+1

                # 다음 노드 진입차수 낮춰주기
                for i in graph[idx+1]:
                    ins[i] -= 1
    
    print('#{0} {1}'.format(T+1, ' '.join(map(str, stack))))
"""

# 순방향 - graph with dictionary
for T in range(10):
    V, E = map(int, input().split())

    ins = [0 for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    graph = {}

    edges = [*map(int, input().split())]

    for e in range(E):
        graph[edges[2*e]] = append(edges[2*e+1])
        ins[edges[2*e+1]] += 1

    stack = [0 for _ in range(V)]
    top = -1
    
    while top < V-1:
        for idx, incount in enumerate(ins[1:]):
            # 진입차수 0인 노드 기준으로 탐색
            if not incount:
                # incount = -1로 설정
                ins[idx+1] -= 1
                if visited[idx+1]:
                    continue
                visited[idx+1] = 1

                # 인덱스 저장
                top += 1
                stack[top] = idx+1

                # 다음 노드 진입차수 낮춰주기
                for i in graph[idx+1]:
                    ins[i] -= 1
    
    print('#{0} {1}'.format(T+1, ' '.join(map(str, stack))))



# 역방향 탐색
# for T in range(10):
#     V, E = map(int, input().split())