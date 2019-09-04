# for T in range(int(input())):
#     max_death = 0

#     # N, M = 6, 3
#     # board = [[N*j+i for i in range(N)] for j in range(N)]
#     # print(board)
#     N, M = map(int,input().split())
#     board = [[*map(int,input().split())] for j in range(N)]

#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             print((i, j), end = ' ')
#             death = 0
#             for di in range(M):
#                 for dj in range(M):
#                     print(board[i+di][j+dj], end=' ')
#                     death += board[i+di][j+dj]
#             print()
#             if max_death < death: max_death = death

#     print(max_death)

for T in range(int(input())):
    max_death = 0

    N, M = map(int,input().split())
    comp = [[0 for _ in range(N-M+1)] for __ in range(N-M+1)]

    for i in range(N):
        row = [*map(int, input().split())]
        for j in range(N-M+1):
            comp[j] = sum(row[j:j+M])


    
        

    board = [[*map(int,input().split())] for j in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            print((i, j), end = ' ')
            death = 0
            for di in range(M):
                for dj in range(M):
                    print(board[i+di][j+dj], end=' ')
                    death += board[i+di][j+dj]
            print()
            if max_death < death: max_death = death

    print(max_death)


"""
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

"""