# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo&categoryId=AWXRFInKex8DFAUo&categoryType=CODE&&&
"""
2차원 평면상의 x, y

"""
from pprint import pprint

def sprint():
    for i in range(N):
        print('i', i, atoms[i], direc[i], energy[i], alive[i])

#------------------------#

# 0 상 1 하 2 좌 3 우
# d 짝수 += 1
# d 홀수 -= 1
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

def checkBoundary(x, y):
    if any((x<0, y<0, x==K, y==K)): return False
    return True

# check collision
def colcheck(x, y, d):
    nx, ny = x + dx[d], y + dy[d]
    print(x, y, nx, ny)
    if checkBoundary(nx, ny):
        # alive[board[y][x][0]] = 0
        return False
    # 인접칸에 원소가 있고 나를 바라보고 있는지
    if board[ny][nx]:
        nd = d-1 if d%2 else d+1
        # if d%2: nd = d-1
        # else: nd = d+1
        if board[ny][nx][1] == nd:
            ci, ni = board[y][x][0], board[ny][nx][0]
            alive[ci] = 0
            alive[ni] = 0
            colli.append(ci)
            colli.append(ni)
            return True
        else:
            return False
    # 인접칸에 원소가 없다면 그 이웃 노드 3개 중 인접칸을 바라보고 있는 원소가 있는지
    else:
        for i in range(4):
            nnx, nny = nx + dx[i], ny + dy[i]
            if nnx == x and nny == y:
                continue
            else:
                if checkBoundary(nnx, nny):
                    if board[nny][nnx]:
                        nd = i-1 if i%2 else i+1
                        if board[nny][nnx][1] == nd:
                            ci, ni = board[y][x][0], board[nny][nnx][0]
                            alive[ci] = 0
                            alive[ni] = 0
                            colli.append(ci)
                            colli.append(ni)
                            return True
                        else:
                            return False
                else: return False

def collide():
    global energySum
    for i in set(colli):
            x, y = atoms[i]
            energySum += energy[i]
            board[y][x] = 0
            atoms[i] = 0

def move():
    global moved
    for i in range(N):
        if alive[i]:
            x, y = atoms[i]
            d = direc[i]
            if y > K and d == 0:
                atoms[i] = 0
                alive[i] = 0
            elif y == 0 and d == 1:
                atoms[i] = 0
                alive[i] = 0
            elif x == 0 and d == 2:
                atoms[i] = 0
                alive[i] = 0
            elif x > K and d == 3:
                atoms[i] = 0
                alive[i] = 0
            else:
                moved = True
                nx, ny = atoms[i][0]+dx[d], atoms[i][1]+dy[d]
                board[ny][nx] = board[y][x]
                board[y][x] = 0
                atoms[i] = [nx, ny]
    


# board size
K = 2001

N = int(input())

atoms = [0 for _ in range(N)]
direc = [0 for _ in range(N)]
energy = [0 for _ in range(N)]
alive = [1 for _ in range(N)]

# board: ()
board = [[[] for _ in range(K)] for __ in range(K)]

# collisioninfo: colliding elements' index
# initialize every time
colli = []

energySum = 0

for i in range(N):
    tmp = [*map(int,input().split())]
    x, y = tmp[0] + K//2, tmp[1] + K//2
    atoms[i] = [x, y]
    board[y][x] = (i, tmp[2])
    direc[i], energy[i] = tmp[2], tmp[3]

# sprint()
# pprint(board)

moved = True
while moved:
    moved = False
    colli = []
    for i in range(N):
        if atoms[i] and alive[i]:
            tmp = (*atoms[i], direc[i])
            print(i, tmp, end=' ')
            if board[tmp[1]][tmp[0]] and alive[i]:
                colcheck(*tmp)
        print(atoms, colli)
        print()
    # print(atoms, colli)
    collide()
    # sprint()
    # pprint(board)
    # print(colli, energySum)

    move()
    finished = True
    for i in range(N):
        if atoms[i]:
            finished = False
    if finished:
        break

print(energySum)

"""
14
-6 5 3 1
-3 5 2 1
-5 2 1 1
3 5 3 1
5 7 1 1
6 7 3 1
7 5 2 1
5 3 0 1
-4 -4 1 1
-4 -6 0 1
5 -3 2 1
4 -6 0 1
6 -4 1 1
9 -7 2 1

"""