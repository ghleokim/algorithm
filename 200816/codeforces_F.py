def check(arr):
    for i in range(len(arr)-1):
        if arr[i] + 2 <= arr[i+1]:
            return False
    return True

t = int(input())

h = [*map(int, input().split())]

can_finish = True
finished = False

changes = []
block = []

while True:
    if can_finish:
        finished = check(h)
        if finished: break

    can_finish = True

    for j in range(len(h)-1):
        if h[j] + 2 <= h[j+1]:
            block.append(j)
        else:
            if len(block) > 0:
                changes.append([*block])
                if len(block) > 1: can_finish = False
                block = []

    if len(block) > 0:
        changes.append([*block])
        if len(block) > 1: can_finish = False
        block = []

    if len(changes) == 0:
        finished = True
    
    for b in changes:
        st = b[0]
        en = b[-1]

        h[st] += 1
        h[en+1] -= 1

        if can_finish and st == en and st > 0:
            can_finish = all((h[st-1]+2 <= h[st], h[en] + 2 <= h[en+1]))

    changes = []
    block = []


print(' '.join(map(str,h)))

"""

n meters away from him

for 1 < j < n

2 6 7 8

3 5 7 8

4 5 6 8

4 5 7 7

4 6 6 7

5 5 6 7


4 6 8 10




if h[j] + 2 <= h[j+1]: h[j] += 1; h[j+1] -= 1; => 이 경우 끝날 수 있음

if h[j] + 2 <= h[j+1] and h[j+1] + 2 <= h[j+2]:
    h[j] += 1; h[j+2] -= 1; => 이 경우 끝나지 않음


every time

    check if needs to be checked
        if finished break

    for j in 0 ~ n-1
        

"""