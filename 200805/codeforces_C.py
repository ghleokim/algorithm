t = int(input())

for _ in range(t):
    n = int(input())
    w = [*map(int, input().split())]
    w_index = [w.count(_) for _ in range(51)]

    max_teams = 0

    for opt_weight in range(2, 101):
        teams = 0
        w_index_cpy = w_index.copy()

        for i in range(n):
            if opt_weight <= w[i]: continue
            elif opt_weight > w[i] + 50: continue
            else:
                other = opt_weight - w[i]
                if w_index_cpy[other] > 0:
                    teams += 1
                    w_index_cpy[other] -= 1

        max_teams = max(max_teams, teams)

    print(max_teams // 2)