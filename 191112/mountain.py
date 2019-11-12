"""

최대 갯수

8 * 8 * 5 * 5 => 완전탐색

for 시작지점(봉우리) []

    for 시작 지점을 제외한 곳에 대해서 공사할 위치 지정

        for 공사 높이 지정

            BFS

"""

def BFS(cur):
    global N
    # print('---------cur:',cur)
    # for i in range(N):
        # print(board[i])
    queue = [(*cur, 1)]
    while queue:
        # print(queue)
        cx, cy, count = queue[0]
        del queue[0]

        for dx, dy in ( (1,0), (-1,0), (0,1), (0,-1) ):
            nx, ny = cx + dx, cy + dy
            if any( (nx < 0, ny < 0, nx > N-1, ny > N-1) ): continue
            
            if board[cx][cy] > board[nx][ny]:
                queue.append((nx,ny,count + 1))
    # print(count)
    return count

def get_height(target):
    global K
    tx, ty = target
    rangeList = {board[tx][ty]}
    for dx, dy in ( (1,0), (-1,0), (0,1), (0,-1) ):
        nx, ny = tx + dx, ty + dy
        if any( (nx < 0, ny < 0, nx > N-1, ny > N-1) ): continue
        
        difference = board[tx][ty] - board[nx][ny]
        if 0 <= difference < K: rangeList.add(board[nx][ny]-1)

    return list(rangeList)
    


for T in range(int(input())):
    max_path = 0

    N, K = map(int,input().split())
    board = [[*map(int,input().split())] for _ in range(N)]

    max_height = max([max(b) for b in board])

    mountains = []

    # 시작 위치 찾기
    for p in range(N*N):
        tx, ty = p % N, p // N
        if board[tx][ty] == max_height: mountains.append((tx,ty))

    # for 시작 위치
    for cur in mountains:
        # 그냥 탐색
        # cur_path = BFS(cur) 
        # if max_path < cur_path: max_path = cur_path

        for position in range(N*N):
            # set position for construction
            # print(position // N, position % N)
            tx, ty = position % N, position // N

            # skip for starting position
            if (tx, ty) == cur: continue

            before = board[tx][ty]
            
            for height in get_height((tx,ty)):
                board[tx][ty] = height
                cur_path = BFS(cur)
                if max_path < cur_path: max_path = cur_path

            board[tx][ty] = before


            # for height in range(1, K+1):
            #     before = board[tx][ty]
            #     if board[tx][ty] < height: continue
            #     board[tx][ty] -= height
            #     # board[tx][ty] = max(board[tx][ty]-height, 0)
                
            #     cur_path = BFS(cur)
            #     if max_path < cur_path: max_path = cur_path
                
            #     board[tx][ty] = before

    # print(max_path)
    print('#', end='')
    print(T+1, max_path)