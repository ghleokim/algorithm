# 0 ~ n 모든 부분집합 구하기

N = 5
visited = [0 for _ in range(N)]

def powerset(n):
    if n == N:
        print(visited)
        return
    else:
        visited[n] = 1
        powerset(n+1)
        visited[n] = 0
        powerset(n+1)

def powerset2(n, case=[]):
    if n == N:
        print(case)
        return
    else:
        case.append(n)
        powerset2(n+1, [*case])
        case.pop()
        powerset2(n+1, [*case])

powerset(0)
powerset2(0)



# 0 ~ n 중 k개 조합

N = 5
case = []
visited = [0 for _ in range(N)]

# for문 중첩탐색
def comb(N, k, n=0):
    if len(case) == k:
        print(case)
        return

    for i in range(n, N):
        case.append(i)
        comb(N, k, n+1)
        case.pop()

print('combination')
comb(5, 3)


a = [[j*N+i for i in range(N)] for j in range(N)]

# error: print(sum(a)) 

print(sum(a,[])) # 배열 차원 down: [0,1,2,3,4,...,24]
print(sum(sum(a,[]))) # 100