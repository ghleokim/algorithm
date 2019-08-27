# 아직
# 가위바위보 결과 table
# if table[card[i]][card[j]]: winner = i
# else: winner = j
table = [[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1]]

def battle(i,j):
    if table[card[i]][card[j]]:
        status[j] = 0
    else:
        status[i] = 0

for T in range(int(input())):
    N = int(input())

    if N % 2:
        N += 1

    status = [1 for _ in range(N)]
    card = [0 for _ in range(N)]

    i = 0
    for t in input().split():
        card[i] = int(t)
        i += 1

    print(card)
    if not card[-1]:
        card[-1] = card[-2]

    print(card)

    tmp = None
    while tmp is None:
        # 각 회차: idx 0 ~ N-1까지
        print(status)
        idx = 0
        tmp = None
        while idx != N:
            if status[idx] and tmp is None:
                tmp = idx
                idx += 1
            elif status[idx] and tmp:
                battle(tmp,idx)
                tmp = None
                idx += 1
            else:
                idx += 1

    print('#{0} {1}'.format(T+1, tmp+1))