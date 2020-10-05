"""
pretest 통과
"""

t = int(input())

for _ in range(t):
    n, l = map(int, input().split())

    A = [*map(int, input().split())]

    p1 = 0
    p2 = l

    v1 = 1
    v2 = 1

    f1 = 0
    f2 = len(A)-1

    flags_passed = [0 for _ in range(n)]

    time = 0

    while True:
        # print(flags_passed)
        if f1 > f2: break
        if all(flags_passed): break

        t1 = abs(A[f1] - p1) / v1
        t2 = abs(A[f2] - p2) / v2

        if t1 < t2:
            time += t1
            p1 = A[f1]
            p2 -= t1 * v2

            flags_passed[f1] = 1
            f1 += 1
            v1 += 1

        elif t1 > t2:
            time += t2
            p1 += t2 * v1
            p2 = A[f2]
            
            flags_passed[f2] = 1
            f2 -= 1
            v2 += 1

        else:
            time += t1

            flags_passed[f1] = 1
            flags_passed[f2] = 1
            p1 = A[f1]
            p2 = A[f2]

            f1 += 1
            f2 -= 1

            v1 += 1
            v2 += 1



    if abs(p2 - p1) > 0:
        remain_time = abs(p2-p1) / (v1 + v2)
        time += remain_time
    
    print('%f' % time)