def getMin(r,c):
    if r == 0:
        B[r][c] = B[r][c] + B[r][c-1]
    elif c == 0:
        B[r][c] = B[r][c] + B[r-1][c]
    else:
        B[r][c] = B[r][c] + min(B[r-1][c], B[r][c-1])

    # print(B)
    return

for T in range(int(input())):
    N = int(input())

    B = [[*map(int, input().split())] for __ in range(N)]

    for r in range(N):
        for c in range(N):
            if r >= N or c >= N:
                continue
            elif r == 0 and c == 0:
                continue
            # print((r,c), end='')
            getMin(r,c)

    print('#', end='')
    print(T+1, B[-1][-1])

