def partition(arr, l, r):
    if l >= r: return

    low = l + 1
    high = r

    while low <= high:
        if arr[low] > arr[l] and arr[high] < arr[l]:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        else:
            if arr[low] <= arr[l]:
                low += 1
            if arr[high] >= arr[l]:
                high -= 1

    arr[l], arr[high] = arr[high], arr[l]

    partition(arr, l, high-1)
    partition(arr, low, r)



for T in range(int(input())):
    N = int(input())
    arr = [*map(int, input().split())]

    partition(arr, 0, len(arr)-1)

    print('#', end='')
    print(T+1, arr[N//2])

"""
1
7
3 2 1 4 5 6 8

"""