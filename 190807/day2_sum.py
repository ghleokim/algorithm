import sys
sys.stdin = open('input.txt', 'r')

# for t in range(10):
#     i = input()
#     testCase = []
#     result = []
#     for i in range(100):
#         testCase.append(list(map(int, input().split())))
#
#     # row sum 100 times : 0 ~ 99, 100 ~ 199, 200
#     for rowIndex in range(100):
#         result.append(sum(testCase[rowIndex]))
#
#     # column sum 100 times : [0, 100, 200,...]
#     for colIndex in range(100):
#         res = 0
#         for rowIndex in range(100):
#             res += testCase[rowIndex][colIndex]
#         result.append(res)
#
#     # diagonal sum 2 times
#     res = 0
#     for i in range(100):
#         res += testCase[i][i]
#     result.append(res)
#     res = 0
#     for i in range(100):
#         res += testCase[i][99-i]
#     result.append(res)
#
#     print('#{0} {1}'.format(t+1, max(result)))

for t in range(10):
    i = input()
    tc, r = [], []
    for i in range(100):
        tc.append(list(map(int, input().split())))

    # for item in tc:
    #     r.append(sum(item))

    # column sum
    r.extend(list(map(sum, zip(*tc))))
    # diagonal sum 2 times
    r1, r2 = 0, 0
    for i in range(100):
        r1 += tc[i][i]
        r2 += tc[i][99-i]
        r.append(r1)
        r.append(r2)
        r.append(sum(tc[i]))

    print('#{0} {1}'.format(t + 1, max(r)))