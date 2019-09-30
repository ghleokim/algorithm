def binarySearch(arr, num):
    left, right = 0, len(arr)-1
    mid = (left+right) // 2
    prev = 0

    while True:
        if arr[mid] == num: return True
        elif arr[mid] > num:
            if prev == 1: return False
            prev = 1
            right = mid - 1
        elif arr[mid] < num:
            if prev == 2: return False
            prev = 2
            left = mid + 1

        mid = (left+right) // 2

for T in range(int(input())):
    N, M = map(int, input().split())
    A = [*map(int, input().split())]
    B = [*map(int, input().split())]
    A.sort()

    count = 0
    for b in B:
        if binarySearch(A, b): count += 1

    print('#', end='')
    print(T+1,count)