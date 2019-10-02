# 완전탐색
ans = 0

"""
for i in range(N):
    if not (i&3): print('left',i)

for i in range(N):
    if i & 3 == 3: print('right', i)

for i in range(N):
    if not (i&12): print('top',i)

for i in range(N):
    if i>>2 == 3: print('bottom',i)
"""

"""N = 4

dx = (1,-1,0,0)
dy = (0,0,1,-1)
def check(choice):
    temp = set()
    for j in range(16):
        if choice & (1 << j):
            row = j // 4
            col = j % 4
            temp.add(arr[row][col])
    res = 1
    for i in range(1,len(temp)+1):
        res *= i
    return res

    

def solve(i,j):
    answer = 0
    queue = [(i,j,0,1<<(i*4+j))]
    while queue:
        print(queue)
        ci,cj,depth,choice = queue[0]
        del queue[0]
        if depth < 7:
            for i in range(4):
                ni,nj = ci+dx[i], cj+dy[i]
                if any((ni<0, nj<0, ni>N-1, nj>N-1)): continue
                queue.append((ni,nj,depth+1,choice + 1<<(ni*4+nj)))
        else:
            if choice in choices: continue
            else:
                choices.append(choice)
                answer += check(choice)

    return answer

choices = []
arr = [[*map(int,input().split())] for _ in range(4)]
result = 0
for i in range(4):
    for j in range(4):
        result += solve(i,j)

print(choices, result)


1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
"""

# first
# def solve(i,j):
#     global result
#     # pos_row, pos_col, depth, visited, string(int)
#     queue = [(i, j, 0, 1<<(i*4+j), arr[i][j])]

#     while queue:
#         ci, cj, depth, choice, res = queue[0]
#         del queue[0]
#         if depth < 6:
#             for k in range(4):
#                 ni, nj = ci+dx[k], cj+dy[k]
#                 if any((ni<0, nj<0, ni>3, nj>3)): continue
#                 # if choice & (1 << (ni*4+nj)): continue
#                 queue.append((ni, nj, depth+1, choice+(1<<(ni*4+nj)), arr[ni][nj]+res*10))
#         else:
#             if res in numbers: continue
#             else:
#                 numbers.append(res)
#                 result += 1
#     return

# dx = (1,-1,0,0)
# dy = (0,0,1,-1)

# for T in range(int(input())):
#     arr = [[*map(int,input().split())] for _ in range(4)]
#     numbers = []
#     result = 0
#     for i in range(4):
#         for j in range(4):
#             solve(i,j)

#     print('#', end='')
#     print(T+1,result)


def solve(i):
    global result
    # pos_row, pos_col, depth, string(int)
    queue = [(i, 0, arr[i])]

    while queue:
        ci, depth, res = queue[0]
        del queue[0]
        if depth < 6:
            for k in range(4):
                if k == 0 and ci % 4 == 3: continue
                elif k == 1 and ci % 4 == 0: continue
                elif k == 2 and ci > 11: continue
                elif k == 3 and ci < 4: continue
                else:
                    ni = ci + di[k]
                    # if any((ni<0, ni>16)): continue
                    queue.append((ni, depth+1, arr[ni]+res*10))
        else:
            if res in numbers: continue
            else:
                numbers.append(res)
                result += 1
    return

di = (1,-1,4,-4)

for T in range(int(input())):
    arr = []
    for _ in range(4):
        arr.extend(map(int,input().split()))
    numbers = []
    result = 0
    for i in range(16):
        solve(i)

    print('#', end='')
    print(T+1,result)
    # print(count)

# import sys
# print(sys.getsizeof(numbers))