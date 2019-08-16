import sys
sys.stdin = open('input.txt', 'r')

def prepend(l, *num):
    return [*num] + l


# 첫 번째 나사부터 시작.
# 두 번째 나사부터 끝까지 전체 길이가 n이 될 때까지 반복.

# s = '2 1 13 2 5 6 4 13 14 5 6 15 25 4 9 16 21 8 12 14 16 11 22 9 20 10 10 21 8 29 11 25 15 22 30 12 29 28 28 30'
# sc = list(map(int, s.split()))
# n = len(sc) // 2

def prepend(l, *num):
    return [*num] + l

def attatch(n, sc):
    temp = [0]

    while len(temp) < n:
        for i in range(1,n):
            bf, af = temp[0], temp[-1]
            # print(temp, bf, af)
            if sc[2*i+1] == sc[2*bf]:
                temp = prepend(temp, i)
            elif sc[2*i] == sc[2*af+1]:
                temp.append(i)

    return temp


for T in range(int(input())):
    n, *s = int(input()), *map(int, input().split())

    res = attatch(n, s)
    result = []
    for num in res:
        result.append(str(s[2*num]))
        result.append(str(s[2*num+1]))

    print('#{0} {1}'.format(T + 1, ' '.join(result)))
#

#     # s: screw // 2 == male, screw // 2 + 1 == female
#
#
#
#     print(checkLeft(n,result,s))
#
#     # result2 = []
#     #
#     # for num in result:
#     #     result2.append(str(s[2*num]))
#     #     result2.append(str(s[2*num+1]))
#
#     # print(' '.join(result2))
#
#     # print('#{0} {1}'.format(T,' '.join(result2)))