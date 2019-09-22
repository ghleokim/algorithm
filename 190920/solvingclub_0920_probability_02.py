import sys
sys.stdin = open('input/input.txt')

def check(visited):
    global result
    res = 1
    for r, c in enumerate(visited):
        if c is not None:
            res *= prob[r][c] / 100
    
    if result < res: return res
    else: return False


def getMax(i = 0, res=1): # i : depth
    global result
    if result >= res: return
    # if not check(visited):
    #     return
    if i == N:
        result = res
        return
    else:
        for j in range(N):
            # print(i, j, visited)
            if visited[j] is not None: continue
            visited[j] = i
            getMax(i+1, res * prob[i][j] / 100)
            visited[j] = None

for T in range(int(input())):
    result = 0
    N = int(input())
    visited = [None for _ in range(N)]
    prob =[[*map(int, input().split())] for _ in range(N)]
    getMax()

    print('#{0} {1:6f}'.format(T+1, result*100))

"""
4
71 51 30 1
29 63 32 93
84 94 33 21
56 40 80 31
"""
