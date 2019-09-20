import sys
sys.stdin = open('input/input.txt')

def cut6(num):
    return int(num * 10 ** 8) / 10 ** 8

# N명의 직원, 1~N까지의 task
def permutation(N, r):
    if r == 0:
        yield t
    else:
        for i in range(N-1,-1,-1):
            arr[i], arr[N-1] = arr[N-1], arr[i]
            t[r-1] = arr[N-1]
            yield from permutation(N-1, r-1)
            arr[i], arr[N-1] = arr[N-1], arr[i]

def getMax(i=0,res=1):
    global max_result, T, nv
    if res < max_result:
        return 0
    if res == 0:
        return 0
    if i == N:
        # print(res, end='')
        nv = [*visited]
        max_result = res
        if T == 0: print(max_result, res); print(visited)

        return res
        
    for j in range(N):
        if visited[j]: continue
        visited[j] = i
        newres = cut6(res * prob[i][j] / 100)
        # if newres == 0: continue
        if newres <= max_result: visited[j] = 0; continue
        # if newres < max_result or newres == 0: continue
        getMax(i+1, newres)
        visited[j] = 0
    

# def getMax2()  

for T in range(int(input())):
    N = int(input())
    visited = [0 for _ in range(N)]
    nv = ''
    t = [0 for _ in range(N)]
    arr = [i for i in range(N)]

    prob = [[*map(int, input().split())] for _ in range(N)]

    max_result = 0.0

    getMax()



    # for case in permutation(N,N):
    #     # print(case)
    #     next = False
    #     result = 1
    #     for i, j in enumerate(case):
    #         result *= prob[i][j] / 100
    #         if result < max_result: next = True; break
    #     if next: continue
    #     if result > max_result:
    #         max_result = result
    # print(nv)
    r = 1
    for k, l in enumerate(nv):
        # print(prob[k][l])
        r *= prob[l][k] / 100
    max_result = r
    print('#{0} {1:8f}'.format(T+1, max_result*100))

"""
1
3
13 0 50
12 70 90
25 60 100
"""