"""
미로
"""
from pprint import pprint

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def checkBoundary(r,c):
    if any((r<0, c<0, r==N, c==N)):
        return False
    return True

    
for T in range(int(input())):
    # BFS
    N = int(input())
    board = [[0 for _ in range(N)] for __ in range(N)]

    for r in range(N):
        incoming = [*map(int, list(input()))]
        for c in range(N):
            if incoming[c]:
                board[r][c] = incoming[c]
                if incoming[c] == 2:
                    pos = (r,c)

    if pos is None:
        print('#{0} 0'.format(T+1))

    else:
        arrival = False
        visited = [[0 for _ in range(N)] for __ in range(N)]

        queue = [pos]
        visited[pos[0]][pos[1]] = 1

        while queue:
            r, c = queue[0]
            del queue[0]
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if checkBoundary(nr,nc):
                    if board[nr][nc] == 3:
                        visited[nr][nc] = 3
                        arrival = True
                        break
                    if not board[nr][nc] and not visited[nr][nc]:
                        queue.append((nr,nc))
                        visited[nr][nc] = 1
            if arrival:
                break

        if arrival:
            print('#{0} 1'.format(T+1))
        else:
            print('#{0} 0'.format(T+1))
        # pprint(visited)

