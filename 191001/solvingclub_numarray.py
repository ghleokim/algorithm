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


N=4
dx = (1,-1,0,0)
dy = (0,0,1,-1)

choices = [0 for _ in range((2**16)+1)]
numbers = [0 for _ in range(10**7)]

def solve(i,j):
    print(i,j)
    global result, count
    queue = [(i, j, 0, 1<<(i*4+j), arr[i][j])]

    while queue:
        ci, cj, depth, choice, res = queue[0]
        del queue[0]
        if depth < 6:
            for k in range(4):
                ni, nj = ci+dx[k], cj+dy[k]
                if any((ni<0, nj<0, ni>N-1, nj>N-1)): continue
                if choice & (1 << (ni*4+nj)): continue
                queue.append((ni, nj, depth+1, choice+(1<<(ni*4+nj)), arr[ni][nj]*(10**(depth+1))+res))
        else:
            count += 1
            if numbers[res]: continue
            else:
                print(bin(choice), res)
                numbers[res] = 1
                result += 1
            # if choices[choice]: continue
            # print(choice,bin(choice))
            # choices[choice] = 1
            # continue


arr = [[*map(int,input().split())] for _ in range(4)]

result = 0
count = 0
for i in range(4):
    for j in range(4):
        solve(i,j)

print(result)
# print(count)