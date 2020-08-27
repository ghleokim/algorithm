def get_candidate(n, s):
    candidate = []
    for k in range(n):
        set_s = set(s[k:k+n])
        candidate.append(['0' in set_s, '1' in set_s])
    return candidate

for _ in range(int(input())):
    n = int(input())
    s = str(input())

    candidate = get_candidate(n, s)

    print('candidates: ', candidate)

    # visit = [[*candi] for candi in candidate]
    # stack = []


    
    # while stack:



    """
    each node:
        visit
        check(choices)
        startpoint k
        candidate = set(s[k:k+n])

        for c in candidate:
            next node, k+1, c
    """
    