"""

input
board

시작 가능한 지점: 

.   x   x   x   x   x   .
.   x   x   x   x   x   .
.   x   x   x   x   x   .

top down

만약 이전에 탐색한 경로의 최대값이(성공한 값)
현재 지점에서 탐색할 수 있는 최대 길이보다 길면 더이상 탐색할 필요가 없다.

N=6이고
    (0,1)에서 탐색할 수 있는 최대길이:
        (N - 1 + N - (N-1) - 1) * 2?

    (n,m)에서 탐색할 수 있는 최대 갚이
       ( (N-m-1) + (N-(n+(N-m-1))-1) )* 2

        N 6 n 0 m 2:  3 + 2 * 2 = 10
        N 6 n 2 m 3:  2 + 1 * 2 = 6

    0   1   2   3   4   5  
0   .   .   x   .   .   .
1   .   x   .   x   .   .
2   x   .   .   o   x   .
3   .   x   o   .   o   x
4   .   .   x   o   x   o
5   .   .   .   x   o   .



# 탐색할 때 bfs?

queue = [(n, m, depth, [현재까지의 경로])]


우하 >> 좌하: d[1] * -1
            d[0] * -1
            d[1] * -1
5
8 2 9 6 6
1 9 3 3 4
8 3 3 3 6
4 3 4 4 9
7 4 6 3 5


"""

from pprint import pprint


N = int(input())

board = [[*map(int,input().split())] for __ in range(N)]

pprint(board)

start = (0,3)

n, m = start
startList = [board[n][m]]

while m > 0:
    n += 1
    m -= 1
    if board[n][m] in startList: break
    startList.append(board[n][m])

print('stlist ', startList)

n, m = start

n += 1
m += 1


while n < N and m < N:
    midList = []
    nn = n
    mm = m
    while mm >= 0 and nn < N and len(midList) < len(startList):
        # print(nn, mm, midList)
        midList.append(board[nn][mm])
        nn += 1
        mm -= 1
    n += 1
    m += 1
    print('midlist' ,midList)

