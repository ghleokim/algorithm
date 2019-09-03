"""
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx

"""

# from pprint import pprint

# board = [[0 for _ in range(15)] for __ in range(5)]

# for i in range(5):
#     for en, c in enumerate(input()):
#         board[i][en] = c

# res = []
# for i in range(15):
#     for j in range(5):
#         if board[j][i]:
#             res.append(board[j][i])

# print(''.join(res))

# pprint(board)

"""
for submit

for T in range(int(input())):
    board = [[0 for _ in range(15)] for __ in range(5)]

    for i in range(5):
        for en, c in enumerate(input()):
            board[i][en] = c

    res = []
    for i in range(15):
        for j in range(5):
            if board[j][i]:
                res.append(board[j][i])

    print('#',end='')
    print(T+1,''.join(res))

"""


from pprint import pprint

for T in range(int(input())):A=[[*input()]+[0]*15 for _ in range(5)];print('#',end='');print(T+1,''.join([''.join([t if t else''for t in z])for z in zip(*A)]))
for T in range(int(input())):print('#',end='');print(T+1,''.join([''.join([t if t else''for t in z])for z in zip(*[[*input()]+[]*15 for _ in range(5)])]))
