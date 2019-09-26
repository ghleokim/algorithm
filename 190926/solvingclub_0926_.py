# powerset
def case(N):
    global min_res, B
    for i in range(1, 2 ** N): # i case
        res = 0
        for j in range(N):  # j 자리수
            if i & 1 << j:
                res += arr[j]
        # print(bin(i), res)
        if res == B: return res
        elif res > B:
            if min_res > res:
                min_res = res
    # print('     ', min_res)
    return min_res

for T in range(int(input())):
    N,B = map(int, input().split())
    min_res = 20 * N * B
    arr = [*map(int,input().split())]
    print('#', end='')
    print(T+1,case(N)-B)
