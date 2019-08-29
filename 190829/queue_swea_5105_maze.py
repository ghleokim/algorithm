dx = (1,-1,0,0)
dy = (0,0,1,-1)

def checkBoundary(x, y):
    if any((x<0,y<0,x>N-1,y>N-1)): return False
    return True


for T in range(int(input())):
    N = int(input())

    board = [[0 for _ in range(N)] for __ in range(N)]
    visited = [[0 for _ in range(N)] for __ in range(N)]

    for i in range(N):
        tmp = [*map(int,input())]
        board[i] = tmp
        for j in range(N):
            if tmp[j] == 2:
                pos = (i,j)

    # print(board)
    # print(pos)

    # 선형 큐
    queue = [[] for _ in range(N**2)]
    front, rear = -1, -1

    rear += 1
    queue[rear] = (*pos, 0)

    while front != rear:
        # print(queue)
        if front == rear:
            front, rear = -1, -1
        
        #dequeue
        front += 1
        x, y, depth = queue[front]
        found = False
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if checkBoundary(nx, ny):
                if board[nx][ny] == 3:
                    found = True
                    break
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    rear += 1
                    queue[rear] = (nx,ny,depth+1)
        
        if found:
            print('#',end='')
            print(T+1,depth)
            break
    else:
        print('#',end='')
        print(T+1,0)