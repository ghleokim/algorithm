def check(arr):
    newarr = sorted(arr)

    for i in range(len(newarr)-2):
        if newarr[i] == newarr[i+1]:
            if newarr[i+1] == newarr[i+2]: return True
        elif newarr[i+1] - newarr[i] == 1:
            if newarr[i+2] - newarr[i+1] == 1: return True
            if newarr[i+1] == newarr[i+2]:
                if i+3 < 6 and newarr[i+3] - newarr[i+1] == 1: return True

    return False


for T in range(int(input())):
    A = []
    B = []
    i = True
    for num in map(int,input().split()):
        if i:
            A.append(num)
            i = False
            continue
        else:
            B.append(num)
            i = True
            continue
    result = 0
    
    for k in range(3, 7):
        print(A[:k], B[:k])
        if check(A[:k]):
            result = 1
            break
        if check(B[:k]):
            result = 2
            break

    print('#', end='')
    print(T+1, result)