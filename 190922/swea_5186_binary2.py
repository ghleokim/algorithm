# 0<N<1인 10진수 N into 2진수
def d2b(num):
    res = ''
    i = -1
    while num != 2 ** i:
        if len(res) > 12: return 'overflow'
        if num - 2 ** i >= 0:
            num -= 2 ** i
            res += '1'
        else:
            res += '0'
        i -= 1
    res += '1'
    return res

for T in range(int(input())):
    N = float(input())
    print('#', end='')
    print(T+1, d2b(N))