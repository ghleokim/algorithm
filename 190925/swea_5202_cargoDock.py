for T in range(int(input())):
    N = int(input())
    se = []
    chosen = []

    for i in range(N):
        se.append([*map(int, input().split())])

    se = sorted(se)

    for i in range(N-1,-1,-1):
        if not chosen:
            count = 1
            chosen.append(se[i])
            head = se[i][0]
        
        elif se[i][0] == se[i-1][0]: continue
        elif head < se[i][1]: continue
        else:
            count += 1
            chosen.append(se[i])
            head = se[i][0]
    print('#', end='')
    print(T+1, count)
    