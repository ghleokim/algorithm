import sys
sys.stdin = open('input/input.txt')

# 방법1 리스트 사용
for T in range(10):
    # 인접행렬
    person = [None for _ in range(101)]

    # BFS, queue
    L, S = map(int, input().split())
    c = [*map(int, input().split())]

    for i in range(L//2):
        if not person[c[2*i]]:
            person[c[2*i]] = [c[2*i+1]]
        else:
            person[c[2*i]].append(c[2*i+1])

    # for i in range(101):
    #     print('i =',i, person[i])


    visited = [0 for _ in range(101)]

    queue = [(person[S], 1)]
    # print(S, queue)
    visited[S] = 1
    max_person = S
    max_depth = 0
    depth = 0



    while queue:
        # print(queue)
        per, depth = queue[0]
        # print(queue[0], max_depth)
        del queue[0]

        for p in per:
            if depth > max_depth and not visited[p]:
                max_depth = depth
                max_person = 0

        for p in per:
            # print(p, end=' ')
            if not visited[p]:
                if depth == max_depth and p > max_person:
                    max_person = p
                # print(p,'|',depth, max_depth,'  ', end=' ')
                    # print(p)
                visited[p] = 1
                if person[p]:
                    queue.append((person[p], depth+1))
    # print()
    # print(person)
    # print(visited)
    print('#',end='')
    print(T+1, max_person)

# queue 직접 구현