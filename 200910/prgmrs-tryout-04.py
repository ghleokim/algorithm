answer = 0
R = 0
C = 0
row_stat_truth = []

def backtrack(A, depth, row_stat, column_stat):
    global R, C, answer, row_stat_truth
    for p in A:
        print('-----' * depth, depth, p)
    print()
    if depth == R * C:
        if any(map(lambda i:i%2, row_stat)) : return
        elif row_stat_truth != row_stat: return
        print('true!!!!!!!')
        answer += 1
    else:
        r = depth // R
        c = depth % C

        if column_stat[c] == 0: return

        for i in range(2):
            A[r][c] = i
            new_row_stat = [*row_stat]
            new_row_stat[r] += i

            new_column_stat = [*column_stat]
            new_column_stat[c] -= 1
           
            backtrack([[A[rr][cc] for cc in range(C)] for rr in range(R)], depth+1, new_row_stat, new_column_stat)

def solution(a):
    global R, C, answer, row_stat_truth
    BIG_NUMBER = 10**7 + 19
    answer = 0
    R = len(a)
    C = len(a[0])

    A = [[0 for _ in range(C)] for __ in range(R)]
    row_stat_truth = [sum([a[_][i] for i in range(C)]) for _ in range(R)]

    row_stat = [0 for _ in range(R)]
    column_stat = [sum([a[i][_] for i in range(R)]) for _ in range(C)]

    backtrack(A, 0, row_stat, column_stat)

    return answer

print(solution([[1,0],[0,1]]))

