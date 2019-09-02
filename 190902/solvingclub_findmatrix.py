import sys

sys.stdin = open('input/input.txt')

for T in range(int(input())):
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)

    # bfs
    def checkBoundary(x,y):
        if any((x<0, y<0, x>N-1, y>N-1)): return False
        return True

    # input
    N = int(input())
    board = [[*map(int,input().split())] for _ in range(N)]

    visited = [[0 for _ in range(N)] for _ in range(N)]

    size = []
    result = []

    for i in range(N):
        for j in range(N):
            if board[i][j] and not visited[i][j]:
                visited[i][j] = 1
                queue = [(i,j)]

                while queue:
                    ci,cj = queue[0]
                    del queue[0]
                    
                    for k in range(4):
                        ni, nj = ci+dx[k], cj+dy[k]
                        if checkBoundary(ni,nj):
                            if board[ni][nj] and not visited[ni][nj]:
                                queue.append((ni,nj))
                                visited[ni][nj] = 1
                
                ri, rj = ci-i+1, cj-j+1
                curSize = ri*rj

                # insertion sort

                if not size:
                    size = [curSize]
                    result = [ri,rj]
                else:
                    for k in range(len(size)-1,-1,-1):
                        if curSize > size[k]:
                            size = size[:k+1] + [curSize] + size[k+1:]
                            result = result[:2*(k+1)] + [ri,rj] + result[2*(k+1):]
                            break
                        elif curSize < size[k]:
                            if k == 0:
                                size = [curSize] + size
                                result = [ri,rj] + result
                            else:
                                continue
                        else:
                            if ri > result[2*k]:
                                size = size[:k+1] + [curSize] + size[k+1:]
                                result = result[:2*(k+1)] + [ri,rj] + result[2*(k+1):]
                            else:
                                continue
                print(size, result)
    
    print(result)
    print('#',end='')
    print(T+1,len(result)//2, *result)
    print()






"""
9
1 1 3 2 0 0 0 0 0
3 2 5 2 0 0 0 0 0
2 3 3 1 0 0 0 0 0
0 0 0 0 4 5 5 3 1
1 2 5 0 3 6 4 2 1
2 3 6 0 2 1 1 4 2
0 0 0 0 4 2 3 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

"""