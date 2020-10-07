"""
선거구 5개

LOGIC

global result = large number = 100 * r * c

for x in range(r)
    for y in range(c)
        get combination of d1, d2 with point x,y

        iterate through combination of d1, d2
            compute all population
            get max_population -min_population
            compare and update global result

"""

"""
validation : d1, d2, sr, sc의 범위를 확인
"""
validation = lambda N, sr, sc, d1, d2: not any([
    d1 < 1,
    d2 < 1,
    sr < 1,
    sc < 1,
    sr + d1 + d2 > N - 1,
    sc - d1 < 0,
    sc + d2 > N - 1
])

def get_combination(N,sr,sc):
    """
        get combination of d1, d2 from sr,sc input

        range of d1 : [1, 2, ..., sc]
        range of d2 : [1, 2, ..., (N-1) - (sr + d1)]
    """
    
    for d1 in range(1, sc+1):
        for d2 in range(1, N - (sr+d1) + 1):
            valid = False

            valid = validation(N,sr,sc,d1,d2)

            if not valid: continue

            yield (d1,d2)

"""
init_district: 전부 구역 5로 차 있는 보드를 생성
"""
def init_district(N):
    return [[5 for _ in range(N)] for __ in range(N)]

def get_population(A, N, sr, sc, d1, d2):
    """
        district 1 :
            r : [0, ... , sr + d1 - 1]
            c : [0, ... , sc - r]
        district 2 :
            r : [0, ... , sr + d2]
            c : [sc + r, ... , N-1]
        district 3 :
            r : [sr + d1, ... , N-1]
            c : if r < sr+d1+d2 -> [0, ... , r - (sr + d1)]
                else            -> [0, ... , sc - 1]
        district 4 :
            r : [sr + d2 + 1, ... , N-1]
            c : if r < sr+d1+d2 -> [ sc + (r - sr+d2) , ... , N-1]
                else            -> [ sc, ... , N-1]
    """
    district = init_district(N)

    for r in range(0, sr+d1):
        for c in range(0, sc+1):
            if r >= sr and c > sc - (r - sr) - 1: continue
            district[r][c] = 1
    
    for r in range(0, sr+d2+1):
        for c in range(sc+1, N):
            if r >= sr and c < sc + (r - sr) + 1: continue
            district[r][c] = 2

    for r in range(sr+d1, N):
        for c in range(0, sc + d2 - d1 + 1):
            if r < sr+d1+d2+1 and c > sc - d1 + (r - sr - d1)-1: continue
            district[r][c] = 3

    for r in range(sr+d2+1, N):
        for c in range(sc + d2 - d1, N):
            if r < sr+d1+d2+1 and c < sc + d2 - (r - sr - d2)+1: continue
            district[r][c] = 4

    pop = [0,0,0,0,0]
    for r in range(N):
        for c in range(N):
            pop[district[r][c]-1] += A[r][c]

    return pop

# START code

# START handle input 
N = int(input())

answer = N * N * 100
A = [[0 for _ in range(N)] for __ in range(N)]

for r in range(N):
    c = 0
    for item in map(int,input().split()):
        A[r][c] = item
        c += 1

# END handle input

# START solve

for sr in range(N):
    for sc in range(N):
        for (d1, d2) in get_combination(N, sr, sc):
            population = get_population(A, N, sr, sc, d1, d2)
            diff = max(population) - min(population)
            answer = min(diff, answer)

print(answer)

# END solve
