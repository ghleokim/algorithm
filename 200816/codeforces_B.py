t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = [*map(int, input().split())]

    k = 1 if k % 2 else 2

    for i in range(k):
        d = max(arr)
        arr = [(d - arr[j]) for j in range(n)]

    print(' '.join(map(str, arr)))

"""
1 2 3 100

99 98 97 0

0 1 2 99

99 98 97 0

...

"""