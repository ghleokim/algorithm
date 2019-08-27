# magnetic
"""
종방향 아래로 탐색할 때 N극이 나오기 전 모든 S극 - 사라진다.
종방향 위로 S극이 나오기 전 모든 N극 - 사라진다.
"""

import sys
sys.stdin = open('input/inputMagnetic.txt')

for T in range(10):
    N = int(input())
    count, board = 0, [[] for _ in range(N)]
    for n in range(N):
        board[n]=[*map(int,input().split())]
    for i in range(N):
        s = 0 # stack
        for j in range(N):
            if board[j][i] == 1:
                s += 1
            elif board[j][i] == 2:
                if s:
                    count += 1
                    s = 0 # empty stack
    
    print('#{0} {1}'.format(T+1, count))

# # shorten
# for T in range(10):
#     N=int(input())
#     c,b=0,[0 for _ in range(N)]
#     for n in range(N): b[n]=[*map(int,input().split())]
#     for i in range(N):
#         s=0
#         for j in range(N):
#             if b[j][i]==1: s+=1
#             elif b[j][i]==2:
#                 if s: c,s=c+1,0
#     print('#{0} {1}'.format(T+1,c))

# # another logic
# for T in range(10):
#     N=int(input())
#     c,s=0,[0 for _ in range(N)]
#     for n in range(N):
#         for e,i in enumerate(input().split()):
#             if i=='1':s[e]+=1
#             elif i=='2' and s[e]:c,s[e]=c+1,0
#     print('#{0} {1}'.format(T+1,c))

# another logic(shorten) 241b | 60,288 kb | 208 ms
# for T in range(10):
#     N=int(input()); c,s=0,[0]*N
#     for n in range(N):
#         for e, i in enumerate(map(int,input().split())):
#             if i==1: s[e]+=1
#             elif i==2 and s[e]: c,s[e]=c+1,0
#     print('#{0} {1}'.format(T+1,c))

# more shorten 230b | 59,560 kb | 198 ms
# for T in range(10):
#     N=int(input());c,s=0,[0]*N
#     for n in range(N):
#         for e,i in enumerate(input().split()):
#             if i=='1':s[e]+=1
#             if i=='2'and s[e]:c,s[e]=c+1,0
#     print('#{0} {1}'.format(T+1,c))


for T in range(10):
    N=int(input());c,s=0,[0]*N
    for n in range(N):
        for e,i in input().split():
            if i=='1':s[e]+=1
            if i=='2'and s[e]:c,s[e]=c+1,0
    print('#{0} {1}'.format(T+1,c))