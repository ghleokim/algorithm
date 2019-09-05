"""

def checkrows(row):
    rowresult = 0
    count = 0

    for i in range(N):
        if count == K and not row[i]:
            rowresult += 1
            count = 0
        elif row[i]:
            count += 1
        else:
            count = 0
    if count == K: rowresult += 1

    return rowresult

for T in range(int(input())):
    N, K = map(int, input().split())
    board = [[*map(int,input().split())] for _ in range(N)]
    result = 0

    for row in board:
        result += checkrows(row)
    for row in [*zip(*board)]:
        result += checkrows(row)

    print('#', end='');print(T+1,result)


"""
# fail
# def C(b):return b.count(K*'1')-b.count('1'*(K+1))
# for T in range(int(input())):
#     N,K=map(int,input().split());B,R=[''.join(input().split())for i in range(N)],0
#     for b in B:R+=C(b)
#     for b in [*zip(*B)]:b=''.join(b);R+=C(b)
#     print('#',end='');print(T+1,R)

