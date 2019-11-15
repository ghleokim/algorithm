"""
N개 중 N//2개를 선택하는 경우를 고려

4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
"""
import sys
sys.stdin = open('input/4012.txt', 'r')

for T in range(int(input())):
    N = int(input())
    S = []
    for row in range(N):
        S.append([*map(int, input().split())])

    choicesA = []
    choicesB = []

    for i in range(1 << N):
        resA, resB = [], []
        for j in range(N):
            if i & (1 << j):
                resA.append(j)
            else:
                resB.append(j)
        # N/2개인 것들만 가르기
        if len(resA) == N//2:
            choicesA.append(resA)
            choicesB.append(resB)
            
    result = None

    for cnt in range(len(choicesA)):
        A, B = 0, 0
        cA, cB = choicesA[cnt], choicesB[cnt]
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                A += S[cA[i]][cA[j]] + S[cA[j]][cA[i]]
                B += S[cB[i]][cB[j]] + S[cB[j]][cB[i]]
        tmp = abs(A-B)
        if result is None:
            result = tmp
        elif result > tmp:
            result = tmp
        else:
            continue
        
    print('#', end='')
    print(T+1,result)






# def countBit(number):
#     global N
#     count = 0
#     for j in range(N):
#         if number & (1 << j): count += 1

#     return bool(count == N//2)

# V=0
# N=6

# for i in range(2**N):
#     print(countBit(i), bin(i))


# def solve(A, B): # A, B: choices
#     global V

#     if countBit(V):
#         print('a', A, bin(A), V)
#         return
#     else:
#         """
#         for i in rane(n):
#             if visietd: continue
#             elsE:
#                 visit 1

#                 visit 0
#         """

#         for j in range(N):
#             if V & (1 << j): continue
#             else:
#                 V += (1<<j)
#                 A += (1<<j)
#                 solve(A,B)
#                 A -= (1<<j) 
#                 V -= (1<<j)
                
# solve(0,0)


# N = int(input())
# board = [[*map(int,input().split())] for _ in range(N)]

# initA, initB, diff = 0, sum([sum(b) for b in board]), sum([sum(b) for b in board])

# for i in range(N):
#     for j in range(N):
#         if i < j:
#             board[i][j] += board[j][i]
#             board[j][i] = 0


