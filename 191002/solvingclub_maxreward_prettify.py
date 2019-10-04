def getMax(num):#quicksort
    n = len(num)
    if n < 2: return num
    else:
        left = getMax(num[:n//2])
        if left is None: return getMax(num[n//2:])
        right = getMax(num[n//2:])
        if right is None: return left

        l,r = 0, 0
        lm, rm = len(left), len(right)
        res = ''

        while l != lm and r != rm:
            if left[l] < right[r]:
                res += right[r]
                r += 1
            else:
                res += left[l]
                l += 1
        if l == lm:
            while r != rm:
                res += right[r]
                r += 1
        else:
            while l != lm:
                res += left[l]
                l += 1
        return res

def resort(num, numlist):
    target = getMax([num[i] for i in numlist])
    num2 = list(num)
    for i in range(len(numlist)):
        num2[numlist[i]] = target[i]

    return num2

for T in range(int(input())):
    num, maxcount = input().split()

    maxcount = int(maxcount)
    num = list(num)

    N = len(num)

    needsort = False
    # 중복 찾기
    numcount = [[] for _ in range(10)]
    for i in range(N):
        numcount[int(num[i])].append(i)
        if not needsort and len(numcount[int(num[i])]) > 1:
            needsort = True
    
    start = 0
    count = 0
    maxnum = list(getMax(num))

    while num != maxnum and count != maxcount:
        for i in range(N):
            if maxnum[i] != num[i]:
                start = i
                break

        left = start
        right = N-1
        k = right-1

        while k > start:
            if num[right] < num[k]:
                right = k
            k -= 1
        
        count += 1
        num[start], num[right] = num[right], num[start]

    if maxcount > count:
        if not needsort and (maxcount-count)//2:
            num[-1], num[-2] = num[-2], num[-1]

    if needsort:
        for numlist in numcount:
            if len(numlist) > 1:
                num = resort(num, numlist)
    
    print('#', end='')
    print(T+1,''.join(num))