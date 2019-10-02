def getMax(num):
    return sorted(list(num))[::-1]

def numsort(nl):
    target = sorted([num[i] for i in nl])[::-1]

    print(target)
    print(nl, num)
    for en, i in enumerate(nl):
        num[i] = target[en]

for T in range(int(input())):
    num, max_count = map(int,input().split())
    
    num = list(str(num))

    numcount = [0 for _ in range(10)]

    for n in num:
        numcount[int(n)] += 1
    
    N = len(num)

    nn = False
    bb = [0 for _ in range(N)]

    numlist = []

    for en, nc in enumerate(numcount):
        nl = []
        if nc > 1:
            for idx, n in enumerate(num):
                if en == int(n):
                    nl.append(idx)
        numlist.append(nl)

    print(numlist)

    for i in range(N):
        if numcount[int(num[i])] > 1:
            nn = True
            bb[i] = num[i]

    print(bb)


    maxnum = getMax(num)

    start = 0
    count = 0

    while maxnum != num:
        if count == max_count:
            break

        for i in range(N):
            if maxnum[i] != num[i]:
                start = i
                break
        
        left = start
        right = N-1

        i = right-1
        while i > start:
            if num[right] < num[i]:
                right = i
            i -= 1

        count += 1
        num[start], num[right] = num[right], num[start]

    if max_count > count:
        if (max_count - count) // 2 and nn:
            num[-1], num[-2] = num[-2], num[-1]

    for nl in numlist:
        if nl:
            numsort(nl)

    print('#', end='')
    print(T+1,''.join(num))


# """
# 32888


# """

326662

626632

666232




