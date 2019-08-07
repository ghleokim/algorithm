# array = [[1,2,3,4,5],
#          [1,2,3,4,5],
#          [1,2,3,4,5],
#          [1,2,3,4,5],
#          [1,2,3,4,5]]
array = [[2,3,2,3,2]] * 5


dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]

result = []

for i in range(len(array)):
    res = []
    for j in range(len(array[i])):
        s=0
        for k in range(4):
            cX = i + dx[k]
            cY = j + dy[k]
            if all((cX >= 0, cX < len(array), cY >= 0, cY < len(array[i]))):
                s += abs(array[i][j] - array[cX][cY])
        res.append(s)
    result.append(res)

a = 0
for l in result:
    a += sum(l)

print(a)