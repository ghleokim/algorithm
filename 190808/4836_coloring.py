from pprint import pprint
# import sys
# sys.stdin = open('input/input4836.txt', 'r')

# check string in 10x10 board
for T in range(int(input())):
    idx, board = [], []

    for i in range(10):
        tmp = []
        for j in range(10):
            tmp.append([])
        board.append(tmp)

    for N in range(int(input())):
        idx.append(input().split())

    for c in idx:
        for i in range(int(c[0]), int(c[2])+1):
            for j in range(int(c[1]), int(c[3])+1):
                board[i][j].append(c[4])

    cnt = 0

    for rows in board:
        for cols in rows:
            if ('1' in cols) and ('2' in cols):
                cnt += 1

    print('#{0} {1}'.format(T+1, cnt))

# ------------------------------ #
