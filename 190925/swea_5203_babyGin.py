# fail
def check(arr):
    head = 0
    tail = 1
    res = False
    while head < 4:
        if arr[tail] is None: break
        if arr[tail] - arr[head] == 1:
            tail += 1
            if arr[tail] is None: break
            elif arr[tail]-arr[head] == 2:
                res = True
                break
            else:
                head = tail
                tail = head + 1
        elif arr[tail] - arr[head] == 0:
            tail += 1
            if arr[tail] is None: break
            elif arr[tail]-arr[head] == 0:
                res = True
                break
            else:
                head = tail
                tail = head + 1
        else:
            head = tail
            tail = head + 1

    return res

def put(num, numarr):
    idx = 0
    for i in range(num):
        if numarr[i]:
            idx += 1
    if not numarr[num]:
        numarr[num] = idx+1
    for i in range(num+1, 10):
        if numarr[i]:
            numarr[i] += 1

    result = [None for _ in range(6)]

    cur = 1
    
    for p, q in enumerate(numarr):
        if q:
            if q > cur:
                while q != cur:
                    result[cur-1] = result[cur-2]
                    cur += 1
            if q == cur:
                result[cur-1] = p
                cur += 1
            
    return result

print(put(2, [0,1,3,0,0,0,0,0,0,0]))


print(check([3,3,3,None,None,None]))
        


for T in range(int(input())):

    A = [None for _ in range(6)]
    B = [None for _ in range(6)]
    Anum = [0 for _ in range(10)]
    Bnum = [0 for _ in range(10)]

    i = 0
    result = 0
    for num in map(int,input().split()):
        if i % 2:
            A = put(num, Anum)
            if i >= 5:
                if check(A) and check(B):
                    result = 0
                elif check(A) and not check(B):
                    result = 2
                    break
                elif check(B) and not check(A):
                    result = 1
                    break
        else:
            B = put(num, Bnum)
            if i >= 4:
                if check(A) and check(B):
                    result = 0
                elif check(A) and not check(B):
                    result = 2
                    break
                elif check(B) and not check(A):
                    result = 1
                    break

        i += 1
    print("#",end='')
    print(T+1,result)