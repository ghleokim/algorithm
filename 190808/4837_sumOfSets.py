def getSum(n, k):
    res = 0
    for i in range(1 << 12):
        # 부분집합의 길이 세기
        cntDigit = 0
        # 원소의 합 세기
        temp = 0
        for j in range(12):
            if i & (1 << j):
                cntDigit += 1
                temp += j+1
        if cntDigit == n:
            if temp == k:
                res += 1
    return res

for T in range(int(input())):
    print('#{0} {1}'.format(T+1, getSum(*map(int,input().split()))))