# N이 홀수일 때, 마름모 그리기
# 1: 1
# 3:
# 0 1 0
# 1 1 1
# 0 1 0
# 5:
# 0 0 1 0 0
# 0 1 1 1 0
# 1 1 1 1 1
# 0 1 1 1 0
# 0 0 1 0 0

a = [[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1]]
N = 5
mid = N // 2
k = 0
offset = 1
for i in range(N):
    print(mid, k, offset)
    for j in range(mid-k, mid+k+1):
        print(' ', j, end=' ')
    print()


    if k == mid: offset *= -1
    k += offset

# for T in range(int(input())):
#     N = int(input())
#     board = [[*map(int,[*input()])] for i in range(N)]
#     mid, k, offset = N//2, 0, 1
#     res = 0
#     for i in range(N):
#         res += sum(board[i][mid-k:mid+k+1])
#         if k == mid: offset *= -1
#         k += offset
#     print('#',end='');print(T+1,res)

#shorten
for T in range(int(input())):m=int(input())//2;print('#',end='');print(T+1,sum([sum([*map(int,[*input()])][abs(i-m):2*m-abs(i-m)+1])for i in range(m*2+1)]))

for T in range(int(input())):m=int(input())//2;print(f'#{T+1} {sum([sum([*map(int,[*input()])][abs(i-m):2*m-abs(i-m)+1])for i in range(m*2+1)])}')


"""
1
5
14054
44250
02032
51204
52212

"""
