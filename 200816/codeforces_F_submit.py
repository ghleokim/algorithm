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
                if len(block) > 2: can_finish = False
                block = []

    if len(block) > 0:
        changes.append([*block])
        if len(block) > 2: can_finish = False
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