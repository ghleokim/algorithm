import sys
sys.stdin = open('input/1953.txt', 'r')

#  0 1 2 3
#  상 하 좌 우
d = ((-1,0), (1,0), (0,-1), (0,1))


table = (
    (),
    (0,1,2,3),  # 1 상하좌우
    (0,1),      # 2 상하
    (2,3),      # 3    좌우
    (0,3),      # 4 상   우
    (1,3),      # 5  하  우
    (1,2),      # 6   하좌
    (0,2)       # 7 상 좌
)

def bfs(pos, L):
    depth = 1
    queue = [(*pos, depth)]
    count = 0
    visited[pos[0]][pos[1]] = 1

    while queue:
        cx, cy, cdepth = queue[0]
        # print(cx, cy, cdepth)
        count += 1
        del queue[0]

        choice = table[board[cx][cy]]
        # print(cx, cy, cdepth, choice, queue)

        for c in choice:
            nx, ny = cx + d[c][0], cy + d[c][1]
            if any(( nx < 0, ny < 0, nx > N-1, ny > M-1 )): continue
            elif not board[nx][ny]: continue
            elif visited[nx][ny]: continue
            elif all([(-d[c][0], -d[c][1]) != dd for dd in [d[e] for e in table[board[nx][ny]] ]]): continue
            else:
                
                if cdepth < L:
                    visited[nx][ny] = 1
                    queue.append((nx,ny, cdepth + 1))
        
    return count
        

for T in range(int(input())):
    N, M, R, C, L = map(int,input().split())
    board = [[*map(int,input().split())] for _ in range(N)]
    visited = [[0 for __ in range(M)] for _ in range(N)]
    
    print('#', end='')
    print(T+1, bfs((R,C), L))

