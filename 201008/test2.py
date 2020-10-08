"""
DFS
"""

def check(arr, case):
    n, sr, sc = case

    res = arr[sr][sc]

    for i in range(n):
        for j in range(n):
            if res != arr[sr+i][sc+j]: return -1
    
    return res

def solution(arr):
    answer = [0,0]



    case = [len(arr), 0, 0]

    stack = [case]

    while stack:
        top = stack[-1]
        del stack[-1]
        
        res = check(arr, top)

        if res == -1:
            n, sr, sc = top
            if n == 1: continue

            n = n // 2
            
            next_case = [
                [n, sr    , sc    ],
                [n, sr + n, sc    ],
                [n, sr    , sc + n],
                [n, sr + n, sc + n]
            ]

            stack.extend(next_case)
            
        else:
            answer[res] += 1

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
    
