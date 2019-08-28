def solve(s, e):
    if s == e: return s
    else:
        win1 = solve(s, (s+e) // 2)
        win2 = solve((s+e) // 2 + 1, e)

        if card[win1] == card[win2]:
            return win1
        else:
            if card[win1] == 1:
                if card[win2] == 2: return win2
                else: return win1
            elif card[win1] == 2:
                if card[win2] == 3: return win2
                else: return win1
            else:
                if card[win2] == 1: return win2
                else: return win1

for T in range(int(input())):
	N = int(input())
	card = [*map(int, input().split())]
	print('#{0} {1}'.format(T+1,solve(0, N-1)+1))


"""
winning table
i j 0 1 2 3
0   0 0 0 0
1   0 1 0 1
2   0 1 1 0
3   0 0 1 1

실패한 코드

table = [[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1]]

def battle(i,j):
    if table[card[i]][card[j]]:
        return True
    else:
        return False

# def battle(i,j):
#     global status
#     if table[card[i]][card[j]]:
#         status[j] = 0
#     else:
#         status[i] = 0

def group(half):
    length = len(half)

    if length % 2:
        length += 1
    
    tmphalf = [0] * length

    for i in range(len(half)):
        tmphalf[i] = half[i]

    if not tmphalf[-1]:
        tmphalf[-1] = tmphalf[-2]

    # print(tmphalf)
    res = []

    tmp = None

    for i in range(length):
        if tmp is None:
            tmp = tmphalf[i]
        else:
            if battle(tmp, tmphalf[i]):
                res.append(tmp)
                tmp = None
            else:   
                res.append(tmphalf[i])
                tmp = None

    return res

for T in range(int(input())):
    N = int(input())

    # 무조건 짝수로 만들기
    if N % 2:
        N += 1

    card = [0]*N
    target = [_ for _ in range(N)]

    # print(target)

    i = 0
    for t in input().split():
        card[i] = int(t)
        i += 1

    if not card[-1]:
        card[-1] = card[-2]

    targetN = N // 2
    left = target[:targetN]
    right = target[targetN:]
    # print(left, right)

    while targetN > 0:
        left = group(left)
        right = group(right)
        targetN //= 2
    # print(left, right)

    if battle(left[0], right[0]):
        print('#{0} {1}'.format(T+1, left[0]+1))
    else:   
        print('#{0} {1}'.format(T+1, right[0]+1))
"""

