# 스도쿠 검증: 가로/세로 /3*3블록 검증
import sys
sys.stdin = open('input/inputSudoku.txt')


# def checkboard(board):
#     for row in board:
#         s = [i for i in range(10)]
#         for r in row:
#             if s[r]: s[r] = 0
#             else: return 0
#     return 1

# def check3b3(board):
#     x = (0,3,6)
#     for i in x:
#         for j in x:
#             row = [b for k in range(j,j+3) for b in board[k][i:i+3]]
#             s = [i for i in range(10)]
#             for r in row:
#                 if s[r]: s[r] = 0
#                 else: return 0
#     return 1


# for T in range(int(input())):
#     print('#{}'.format(T+1),end=' ')
#     board = [[*map(int,input().split())] for _ in range(9)]
#     if checkboard(board) and checkboard([*zip(*board)]) and check3b3(board): print(1)
#     else: print(0)
    

# set

def cr(row):return 1 if len(set(row))==9 else 0
def cb(B):return 1 if all([cr(row)for row in B])else 0
def c3(B):
    x = (0,3,6)
    for m,n in [(i,j) for i in x for j in x]:
        row=[b for k in range(n,n+3) for b in B[k][m:m+3]]
        if not cr(row): return 0
    return 1
for T in range(int(input())):print('#{}'.format(T+1),end=' ');B=[[*map(int,input().split())]for _ in range(9)];print(1 if cb(B)and cb([*zip(*B)])and c3(B) else 0)


