for T in range(int(input())):
    n = int(input())

    A = [0 for _ in range(n)]
    B = [0 for _ in range(n)]

    AminusB = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]

    for i in range(n):
        ai, bi = map(int, input().split())  
        A[i], B[i] = ai, bi
        AminusB[i] = (ai - bi, i)

    AminusB.sort()

    score_a = 0
    score_b = 0

    ai = n-1
    bi = 0

    for i in range(n):
        if i % 2: # B
            while True:
                if visited[AminusB[bi][1]] == 0: break
                bi += 1
            diff, vi = AminusB[bi]
            score_b += B[vi]
            visited[vi] = 1

        else: # A
            while True:
                if visited[AminusB[ai][1]] == 0: break
                ai -= 1
            diff, vi = AminusB[ai]
            score_a += A[vi]
            visited[vi] = 1
    
    print('ans,',score_a - score_b, score_a, score_b)
    print(AminusB)