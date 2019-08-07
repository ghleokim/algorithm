a = [1,2, -4, 3, 4, 5, -7, 1]

n = len(a)
cnt = 0

for i in range(1 << n): # 부분집합의 갯수만큼 돌린다.
    res = []
    for j in range(n): # 원소의 수 만큼 비교
        if i & (1 << j):
            res.append(a[j])
    if sum(res) == 0:
        cnt += 1
        print(res)

print(cnt)