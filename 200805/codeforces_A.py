t = int(input())

for i in range(t):
    n = int(input())
    arr = [*map(int, input().split())]
    res = False

    if n == 1:
        print("YES")
        continue

    arr = list(set(arr))
    arr.sort()

    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > 1:
            print("NO")
            res = True
            break

    if res == False:
        print("YES")