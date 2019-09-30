def bottom_up(arr):
    temp = [0 for _ in range(arr[0])]
    temp[-2] = 1
    res = arr[0]
    idx = res-2
    while idx != 1:
        # print(idx, temp, temp[idx:idx+arr[idx]])
        res = min(temp[idx:idx+arr[idx]])+1
        idx -= 1
        temp[idx] = res
    
    return min(min(temp[idx:idx+arr[idx]]), res)

for T in range(int(input())):
    print('#', end='')
    print(T+1,bottom_up([*map(int,input().split())]))