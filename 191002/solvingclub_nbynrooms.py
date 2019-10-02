# bfs
"""
def bfs(i,j):
    if paths[i][j]: return paths[i][j]
    nextroom = False
    for k in range(4):
        ni,nj = i+dx[k], j+dy[k]
        if any((ni<0, nj<0, ni>N-1, nj>N-1)): continue
        elif arr[ni][nj]-arr[i][j] == 1:
            nextroom = True
            break
    if nextroom:
        if paths[ni][nj]: return paths[ni][nj]+1
        else:
            return bfs(ni,nj)+1
    else:
        return 1


dx = (0,0,1,-1)
dy = (1,-1,0,0)

for T in range(int(input())):
    N = int(input())
    arr = [[*map(int,input().split())] for _ in range(N)]
    paths = [[0] * N for _ in range(N)]

    # print(paths,arr)
    max_path = 0
    max_path_num = N**2+1

    for i in range(N):
        for j in range(N):
            paths[i][j] = bfs(i,j)
            if paths[i][j] > max_path:
                max_path = paths[i][j]
                max_path_num = arr[i][j]
            elif paths[i][j] == max_path:
                if max_path_num > arr[i][j]:
                    max_path_num = arr[i][j]

    print(paths)
    print('#', end='')
    print(T+1, max_path_num, max_path)
"""


# def seek(i,j):
#     find = arr[i][j]+1
#     for k in range(4):
#         ni,nj = i+dx[k], j+dy[k]
#         if any((ni<0, nj<0, ni>N-1, nj>N-1)): continue
#         elif arr[ni][nj] == find:
            
#             break
#     else:
#         paths[i][j] = 1
#         return 1

#     if paths[ni][nj]:
#         paths[i][j] = paths[ni][nj] + 1
#         return paths[ni][nj]+1
#     else:
#         paths[i][j] = seek(ni,nj)+1
#         return seek(ni,nj)+1

def seek(i,j):
    







dx = (0,0,1,-1)
dy = (1,-1,0,0)

for T in range(int(input())):
    N = int(input())
    arr = [[*map(int,input().split())] for _ in range(N)]
    paths = [[0] * N for _ in range(N)]

    max_path = 0
    max_path_num = N**2+1

    for i in range(N):
        for j in range(N):
            if not paths[i][j]:
                paths[i][j] = seek(i,j)

            if paths[i][j] > max_path:
                max_path = paths[i][j]
                max_path_num = arr[i][j]
            elif paths[i][j] == max_path:
                if max_path_num > arr[i][j]:
                    max_path_num = arr[i][j]

    print(paths)
    print('#', end='')
    print(T+1, max_path_num, max_path)
