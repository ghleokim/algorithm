"""
tc 10개.
도착점 표시
1)
거꾸로 올라오면서 좌우에 길이 있는지 확인
2)
row 받으면서 시작점으로부터의 index를 가지고 위치 계속 추적

0 4 6 9
0 4 9 6
0 9 4 6
9 0 6 4
0 9 6 4
0 6 9 4
"""

import sys
sys.stdin = open('input.txt', 'r')
"""
for T in range(10):
    input()
    sidx = []
    startrow = input()
    en = 0
    for c in startrow[::2]:
        if c == '1':
            sidx.append(en)
        en += 1   

    sidx.extend(sidx) 
    # print(sidx)
    initial = sidx.copy()
    
    # print(sidx, startrow)
    for _ in range(99):
        row = input()
        for idx in range(1, len(initial)):
            if row[2*(initial[idx]-1)] == '1':
                sidx[idx], sidx[idx-1] = sidx[idx-1], sidx[idx]
    
    c = 0
    for i in row[::2]:
        if ord(i) == 50:
            print('#{0} {1}'.format(T+1, sidx[c]))
            break
        if ord(i) == 49:
            c += 1
"""
#--------------------#
"""
for T in range(10):
    input()
    row = input()
    sidx = [0] * 100
    initial = []
    for i in range(100):
        if row[2*i] == '1':
            sidx[i] = i
            initial.append(i)
    # print(sidx, initial)
    
    for _ in range(99):
        row = input()
        for idx in range(1, len(initial)):
            comp = (initial[idx-1], initial[idx])
            if row[2*(comp[1]-1)] == '1':
                sidx[comp[0]], sidx[comp[1]] = sidx[comp[1]], sidx[comp[0]]
                # print(sidx)
    
    for j in range(100):
        if row(2*j) == '2':
            print('#{0} {1}'.format(T+1,sidx[j]))
    # for j in range(len(initial)):
    #     if row[2*initial[j]] == '2':
    #         print('#{0} {1}'.format(T+1, sidx[initial[j]]))
"""
# ------------------------------------------ #

for T in range(10):
    input()
    board = []
    for _ in range(100):
        board.append([*map(int,input().split())])

    for en, c in enumerate(board[99]):
        if c == 2:
            current = en

    for row in board[::-1]:
        if current == 0:
            if row[1]:
                latter = current+1
                while row[latter]:
                    latter += 1
                    if latter == 100:
                        break
                current = latter - 1
            else:
                continue
        elif current == 99:
            if row[98]:
                if row[current-1]:
                    former = current-1
                    while row[former]:
                        former -= 1
                        if former < 0:
                            break
                    current = former + 1
            else:
                continue
        else:
            if row[current-1]:
                former = current-1
                while row[former]:
                    former -= 1
                    if former < 0:
                        break
                current = former + 1
            elif row[current+1]:
                latter = current+1
                while row[latter]:
                    latter += 1
                    if latter == 100:
                        break
                current = latter - 1
            else:
                continue

    print('#{0} {1}'.format(T+1, current))