# # 2차 배열 선택 정렬
#
from pprint import pprint
#
# arr = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
#
# for i in range(len(arr)*len(arr[0])):
#     xi = i // 5
#     yi = i % 5
#     temp = [xi, yi]
#
#     for idx in range(i, 25):
#         if arr[idx // 5][idx % 5] < arr[temp[0]][temp[1]]:
#             temp = [idx // 5, idx % 5]
#
#     arr[xi][yi], arr[temp[0]][temp[1]] = arr[temp[0]][temp[1]], arr[xi][yi]
#
#     print(arr)

# 원하는 순서로 정렬: 달팽이
targetArr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

boundary = [[0, 4], [0, 4]] # min(x), max(x), min(y), max(y)

target = [0,0]
cDir = 0
direction = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(25):
    targetArr[target[1]][target[0]] = '{0:>2}'.format(i+1)
    # print(target)
    if cDir == 0 and target[0] == boundary[0][1]: # moving east
        cDir = 1
        boundary[1][0] += 1
    elif cDir == 1 and target[1] == boundary[1][1]: # moving south
        cDir = 2
        boundary[0][1] -= 1
    elif cDir == 2 and target[0] == boundary[0][0]: # moving west
        cDir = 3
        boundary[1][1] -= 1
    elif cDir == 3 and target[1] == boundary[1][0]: # moving north
        cDir = 0
        boundary[0][0] += 1

    target[0] += direction[cDir][0]
    target[1] += direction[cDir][1]


    pprint(targetArr)