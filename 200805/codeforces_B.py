"""
n gifts


"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    
    a_min = min(a)
    b_min = min(b)

    a_moves = [a[i] - a_min for i in range(n)]
    b_moves = [b[i] - b_min for i in range(n)]

    res = 0

    for j in range(n):
        res += max(a_moves[j], b_moves[j])

    print(res)