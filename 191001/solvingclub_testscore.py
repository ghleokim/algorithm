# Dynamic Programming
# 문제의 갯수 N, 배점 m1, m2, m3, m4, ..., mn
"""
def arrAdd(arr, orig, k):
    newarr = arr[1:] + [arr[0]]
    for i in range(len(arr)):
        newarr[i] += orig[(k) // len(arr)]
    return newarr

for T in range(int(input())):
    N = int(input())
    M = [*map(int, input().split())]
    ans = [0 for _ in range(100*100+1)]
    count = 0

    newarr = [*M]
    maxnum = sum(M)

    for i in range(N):
        print(newarr)
        for j in range(N):
            # if newarr[i] > maxnum: continue
            if not ans[newarr[j]]:
                ans[newarr[j]] += 1
                count += 1
        newarr = arrAdd(newarr, M, i)
    
    print(ans[:maxnum])

    print('#', end='')
    print(T+1, count+1)

"""

# 부분집합 - 시간초과


def case(N):
    global count, ans
    for i in range(2**N):
        cur = 0
        for j in range(N):
            if i & (1 << j):
                cur += arr[j]
        if not ans & (1 << cur):
            print(cur)
            ans += 1 << cur
            count += 1
    
for T in range(int(input())):
    N = int(input())
    ans = 0
    arr = [*map(int,input().split())]
    count = 0
    case(N)

    print('#', end='')
    print(T+1,count)

# reduce arr
N = int(input())
arr = [*map(int,input().split())]
maxnum = max(arr)

cnt = [0 for _ in range(maxnum+1)]

for i in range(N):
    cnt[arr[i]] += 1

newarr = []

for n, c in enumerate(cnt):
    if c: newarr.append(n)

# for i in range(N-1, -1, -1):
#     print(arr[i])
#     for j in range(1, cnt[arr[i]]):
#         print('     ', i, j)

print(newarr)
i = len(newarr)-1

while i != -1:
    print('i', i)
    num = newarr[i]
    repeat = False
    for j in range(2, cnt[num]+1):
        print(' ',i,j)
        if num * (j+1) > maxnum: continue
        if cnt[num * (j+1)]:
            repeat = True
            cnt[num] += (j+1)*cnt[num*(j+1)]
            cnt[num*(j+1)] = 0
    
    print('cnt', cnt)
    if not repeat:
        i -= 1

result = 1
for n, c in enumerate(cnt):
    if c: result *= c+1

print(result)

"""
5
1 1 1 3 6


8
2 2 2 6 6 10 20 70
6
2 2 2 6 10 20 
3
5 10 15
5
1 3 4 5 10

"""

# #submit
# for T in range(int(input())):
#     N = int(input())
#     arr = [*map(int,input().split())]
#     maxnum = max(arr)

#     cnt = [0 for _ in range(maxnum+1)]

#     for i in range(N):
#         cnt[arr[i]] += 1

#     newarr = []

#     for n, c in enumerate(cnt):
#         if c: newarr.append(n)

#     i = len(newarr)-1

#     while i != -1:
#         num = newarr[i]
#         repeat = False
#         for j in range(2, cnt[num]+1):
#             if num * (j+1) > maxnum: continue
#             if cnt[num * (j+1)]:
#                 repeat = True
#                 cnt[num] += (j+1)*cnt[num*(j+1)]
#                 cnt[num*(j+1)] = 0
#         if not repeat:
#             i -= 1

#     result = 1
#     for n, c in enumerate(cnt):
#         if c: result *= c+1

#     print('#', end='')
#     print(T+1,result)