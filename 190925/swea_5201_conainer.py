def merge(arr, start, end):
    if start == end:
        # print(start)
        return [start]
    else:
        mid = (start + end) // 2
        a = merge(arr, start, mid)
        b = merge(arr, mid + 1, end)
        # print(a, b, 'start', start, end)

        ai, bi, al, bl = 0, 0, len(a), len(b)
        
        cur = 0
        newarr = [None] * (end-start+1)

        while ai != al and bi != bl:
            left = arr[a[ai]]
            right = arr[b[bi]]
            # print('lr', left, right, 'aibi', ai, bi, al, bl)

            if left >= right:
                newarr[cur] = b[bi]
                bi += 1
            else:
                newarr[cur] = a[ai]
                ai += 1
            cur += 1

        # print(cur, ai, bi)
        if ai != al:
            while ai != al:
                newarr[cur] = a[ai]
                cur += 1
                ai += 1
        else:
            while bi != bl:
                newarr[cur] = b[bi]
                cur += 1
                bi += 1
        return newarr

for T in range(int(input())):
    N, M = map(int, input().split())
    wi = [*map(int, input().split())]
    ti = [*map(int, input().split())]

    result = 0

    wi_Sorted = [wi[i] for i in merge(wi, 0, N-1)]
    ti_Sorted = [ti[i] for i in merge(ti, 0, M-1)]
    # print(wi_Sorted, ti_Sorted)

    windex = N-1
    tindex = M-1

    while tindex >= 0:
        # print(windex, tindex)
        if ti_Sorted[tindex] >= wi_Sorted[windex]:
            result += wi_Sorted[windex]
            windex -= 1
            tindex -= 1
        else:
            windex -= 1

        if windex < 0:
            break

    print('#', end='')
    print(T+1, result)