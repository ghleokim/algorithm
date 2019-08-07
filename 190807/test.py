# tc = [[1,2,3,4,5],
#       [1,2,3,4,5],
#       [1,2,3,4,5],
#       [1,2,3,4,5],
#       [1,2,3,4,5]]
#
#
# print(list(map(sum, zip(*tc))))
#

arr = [3,6,7,1,5,4]

n = len(arr)
for i in range(1 << n):
    for j in range(n+1):
        if i & (1 << j):
            print(arr[j], end=',')
    print()


