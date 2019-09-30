# visited 이용한 backtracking
def backtrack(arr, depth=0, res=0):
    global minSum
    if depth == N:
        minSum = res
        return
    else:
        for i in range(N):
            if res + arr[depth][i] > minSum: continue
            if visited[i]: continue
            else:
                visited[i] = 1
                backtrack(arr, depth+1, res + arr[depth][i])
                visited[i] = 0

for T in range(int(input())):
    N = int(input())
    minSum = 100 * N
    table = [[*map(int,input().split())] for _ in range(N)]
    visited = [0 for _ in range(N)]

    backtrack(table)

    print('#',end='')
    print(T+1,minSum)


# binary visited를 이용한 backtracking
def backtrackbin(arr, depth=0, res=0):
    global minSum, visitedbin
    if depth == N:
        minSum = res
        return
    else:
        for i in range(N):
            if res + arr[depth][i] > minSum: print('skip');continue
            if visitedbin & (1 << i): continue
            else:
                visitedbin += 1 << i
                backtrackbin(arr, depth+1, res + arr[depth][i])
                visitedbin -= 1 << i

for T in range(int(input())):
    N = int(input())
    minSum = 100 * N
    table = [[*map(int,input().split())] for _ in range(N)]
    visitedbin = 0

    backtrackbin(table)

    print('#',end='')
    print(T+1,minSum)

