# def search(i):
#     top = 0
#     stack[top] = i
#     while top != -1:
#         #pop
#         cur = stack[top]
#         top -= 1

#         for k in range(1,N+1):
#             if arr[cur][k] and not visited[k]:
#                 #append
#                 top += 1
#                 stack[top] = k
#                 visited[k] = 1

# for T in range(int(input())):
#     N, M = map(int,input().split())
#     arr = [[0] * (N+1) for _ in range(N+1)]
#     for _ in range(M):
#         i,j = map(int,input().split())
#         arr[i][j] = 1
#         arr[j][i] = 1

#     visited = [0 for _ in range(N+1)]
#     stack = [0 for _ in range(N*N)]
#     count = 0


#     for i in range(1,N+1):
#         if not visited[i]:
#             count += 1
#             search(i)

#     print('#', end='')
#     print(T+1,count)

# =============== #
# binary counting

def search(i):
    global visited
    top = 0
    stack[top] = i
    while top != -1:
        #pop
        cur = stack[top]
        top -= 1

        for k in range(1,N+1):
            if arr[cur][k] and not visited & (1<<k):
                #append
                top += 1
                stack[top] = k
                visited += (1<<k)
                # visited[k] = 1

for T in range(int(input())):
    N, M = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        i,j = map(int,input().split())
        arr[i][j] = 1
        arr[j][i] = 1

    visited = 0
    # visited = [0 for _ in range(N+1)]
    stack = [0 for _ in range(N*N)]
    count = 0


    for i in range(1,N+1):
        if not visited & (1<<i):
            count += 1
            search(i)
        # if not visited[i]:
        #     count += 1
        #     search(i)
            
    print('#', end='')
    print(T+1,count)