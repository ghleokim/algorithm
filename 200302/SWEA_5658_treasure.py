def getNumbers(N, num, appending=''):
    unit = N // 4
    return [num[0:unit], num[unit:2*unit], num[2*unit:3*unit], num[3*unit:] + appending]


def solve(N, K, num):
    # N, K = 12, 10 # map(int, input().split())
    # num = '1B3B3B81F75E'

    unit = N // 4
    res = set()

    for i in range(unit):
        # print(i, num[i:], num[:i])
        for elem in getNumbers(N, num[i:], num[:i]): res.add(elem)

    return int(sorted([*res])[-K], base=16)


for T in range(int(input())):
    N, K = map(int, input().split())
    print(f'#{T+1}', solve(N,K,input()))
