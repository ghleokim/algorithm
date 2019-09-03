import sys
sys.stdin = open('input/input.txt')

def seek(x,y):
    # print(x, y, end=' ')
    row, col = 1, 1
    while y + col < N and board[x][y+col]:
        col += 1
    while x + row < N and board[x+row][y]:
        row += 1
    # print(row,col)
    return row, col



for T in range(int(input())):
    # input
    N = int(input())
    board = [[*map(int,input().split())] for __ in range(N)]

    result = []

    for i in range(N):
        for j in range(N):
            if board[i][j] and any((i==0, board[i-1][j]==0)) and any((j==0, board[i][j-1]==0)):
                result.append(seek(i,j))

    print('#',end='')
    print(T+1,len(result),*map(lambda x: ' '.join(map(str,x)), sorted(result, key=lambda x: (x[0] * x[1], x[0]))))
    



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