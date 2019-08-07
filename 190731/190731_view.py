#! 190731
#

# compare = list(map(int, a.split()))
#
# bubble sort
#
# for c in range(len(compare), -1, -1):
#     for d in range(c-1):
#         if compare[d] > compare[d + 1]:
#             compare[d], compare[d + 1] = compare[d + 1], compare[d]
# print(compare)

# ### exhaustive method
# for enum in range(10):
#     length = input()
#     building = list(map(int, input().split()))
#     result = 0
#     for i in range(2, len(building)-2):
#         compare = [0] * 4
#         if building[i] > building[i+2] and building[i] > building[i-2]:
#             if building[i] > building[i+1] and building[i] > building[i-1]:
#                 compare[0] = building[i] - building[i-2]
#                 compare[1] = building[i] - building[i-1]
#                 compare[2] = building[i] - building[i+1]
#                 compare[3] = building[i] - building[i+2]
#
#                 for c in range(4, -1, -1):
#                     for d in range(c - 1):
#                         if compare[d] > compare[d + 1]:
#                             compare[d], compare[d + 1] = compare[d + 1], compare[d]
#
#                 result += compare[0]
#
#     print('#{0} {1}'.format(enum + 1, result))

## improvement

for en in range(10):
    length = int(input())
    b = list(map(int, input().split()))
    result = 0
    index = 2

    while index < length-2:
        i = index
        # current value is smaller than others
        if b[i+2] > b[i] or b[i+1] > b[i] or b[i-1] > b[i] or b[i-2] > b[i]:
            if b[i+2] > b[i+1]:
                index = i + 2
            elif b[i+1] > b[i-1]:
                index = i + 1
            else:
                index = i + 3
        # current value is the largest
        else:
            ref = [b[i]-b[i-2], b[i]-b[i-1], b[i]-b[i+1], b[i]-b[i+2]]

            for c in range(4, -1, -1):
                for d in range(c - 1):
                    if ref[d] > ref[d + 1]:
                        ref[d], ref[d + 1] = ref[d + 1], ref[d]

            result += ref[0]
            index = i + 3

    print('#{0} {1}'.format(en + 1, result))

### with library
for en in range(10):
    length, b = (int(input()), list(map(int, input().split())))

    # i=0
    # for num in b[i:i+6:]:

    print('#{0} {1}'.format(en + 1, result))

