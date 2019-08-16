# import sys
# sys.stdin = open('input/input4843.txt', 'r')

# 선택정렬 후 참조
def specialSort(target):
    t = target.copy()
    for i in range(len(t)):
        tmpIdx = i
        for idx in range(i, len(t)):
            if t[idx] < t[tmpIdx]:
                tmpIdx = idx
        t[tmpIdx], t[i] = t[i], t[tmpIdx]

    res =[]

    for _ in range(5):
        res.append(t.pop(-1))
        res.append(t.pop(0))

    return res

for T in range(int(input())):
    N, *a = input(), *map(int, input().split())
    result = specialSort(a)
    print('#{0} {1}'.format(T+1, ' '.join(map(str, result))))

# ----------------------------- #

# #실패
# def specialSort(target):
#     t = target.copy()
#     N = len(t) // 2
#     r = len(t) % 2
#     if t[0] < t[1]:
#         t[0], t[1] = t[1], t[0]
#
#     for i in range(N+r): # 반복횟수
#         minT, maxT = i*2+1, i*2
#         for j in range(2*i, len(t)):
#             if t[minT] > t[j]:
#                 minT = j
#             elif t[maxT] < t[j]:
#                 maxT = j
#         t[maxT], t[2*i] = t[2*i], t[maxT]
#         t[minT], t[2*i+1] = t[2*i+1], t[minT]
#
#
#
#     return t
#
# for T in range(int(input())):
#     N, *a = input(), *map(int, input().split())
#     result = specialSort(a)[:10]
#     print('#{0} {1}'.format(T+1, ' '.join(map(str, result))))
#
# # ab = '2 1 13 2 5 6 4 13 14 5 6 15 25 4 9 16 21 8 12 14 16 11 22 9 20 10 10 21 8 29 11 25 15 22 30 12 29 28 28 30'
# # a = list(map(int, ab.split()))
# #
# # result = specialSort(a)
# # print('#{0} {1}'.format(1, ' '.join(map(str, result))))
