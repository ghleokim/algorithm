def merge(arr, start, end):
    global count
    if start == end:
        return [arr[start]]
    else:
        mid = (start + end + 1) // 2
        left = merge(arr, start, mid-1)
        right = merge(arr, mid, end)
        # print(left, right)

        if not left: return right
        elif not right: return left

        li, ri = 0, 0
        L, R = mid-start, end+1 - mid

        residx = 0
        res = [0 for i in range(end+1-start)]

        while li != L and ri != R: # left right 원소 하나씩 비교
            if left[li] > right[ri]:
                res[residx] = right[ri]
                ri += 1
            else:
                res[residx] = left[li]
                li += 1
            residx += 1
        
        if li == L: # 남은 원소 집어넣기
            while ri != R:
                res[residx] = right[ri]
                ri += 1
                residx += 1
        elif ri == R:
            count += 1
            while li != L:
                res[residx] = left[li]
                li += 1
                residx += 1
        return res

for T in range(int(input())):
    N = int(input())
    arr = [*map(int, input().split())]
    count = 0
    print('#', end='')
    print(T+1, merge(arr, 0, N-1)[N//2], count)