t = int(input())


def solve(n, A, B, C):
    stack = []
    visited = [[0 for _ in range(n)] for __ in range(3)]

    ABC = [A,B,C]

    j = 0

    while j < n:
        candidates = [col[j] for col in ABC]
        print(candidates)

        found = False
        for jj in range(3):
            if j > 0 and candidates[jj] == stack[-1]: continue
            elif visited[jj][j]: continue
            found = True
            stack.append(candidates[jj])
            visited[jj][j] = 1
            break
            
        if not found:
            del stack[-1]
            j -= 1
        
        j += 1

    return stack
        
            

for _ in range(t):
    n = int(input())

    A = [*map(int, input().split())]
    B = [*map(int, input().split())]
    C = [*map(int, input().split())]

    P = solve(n, A, B, C)

    print(' '.join(map(str, P)))
