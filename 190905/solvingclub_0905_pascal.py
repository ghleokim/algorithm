#pr: former row
# newrow = [1]+[pr[i]+pr[i+1] for i in range(len(pr)-1)]+[1]
# print(newrow)

# # 1
for T in range(int(input())):
    pc, N = [[1]], int(input())
    for i in range(2,N+1): pc.append([1]+[pc[-1][i]+pc[-1][i+1] for i in range(i-2)]+[1])
    print('#{}'.format(T+1))
    for i in range(N):print(*pc[i])

# 2