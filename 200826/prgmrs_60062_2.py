def permutation(arr):
    length = len(arr)
    candidate = list(set(arr))
    count = [arr.count(i) for i in range(100)]

    result = []

    for first in candidate:
        stack = []
        new_count = [*count]

        new_count[first] -= 1
        stack.append([[first], new_count])

        while stack:
            top, top_count = stack.pop()

            if len(top) == length:
                result.append(top)
                continue

            for c in candidate:
                if top_count[c] > 0:
                    new_top_count = [*top_count]
                    new_top_count[c] -= 1
                    item = [[*top, c], new_top_count]
                    stack.append(item)
            
    return result

def fix(path_offset, perm): # (가야할 거리, 갈 수 있는 거리)
    path_i = 0
    perm_i = 0
    moved = False

    while path_i < len(path_offset):
        # print('after : ', perm)
        # print('path', path_i, 'perm', perm_i)
        if perm_i == len(perm):
            return -1
        elif path_offset[path_i] > perm[perm_i]:
            if not moved: return -1
            else:
                moved = False
                perm_i += 1
        else:
            perm[perm_i] -= path_offset[path_i]
            path_i += 1
            moved = True
    return perm_i + 1

def solution(n, weak, dist):
    answer = -1
    if len(weak) == 1:
        return 1

    for direction in (1,-1):
        for ent_index in range(len(weak)):
            path = [weak[(ent_index + direction * i) % len(weak)] + (ent_index + direction * i) // len(weak) * n for i in range(len(weak))]
            path_offset = [abs(path[j+1]-path[j]) for j in range(len(weak)-1)]

            for perm in permutation(dist):
                res = fix(path_offset, [*perm])
                print(path, path_offset, perm, res)
                if answer == -1:
                    answer = res
                else:
                    answer = min((999 if res == -1 else res), answer)                

    return answer

print(solution(	12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1,5,6,10], [3,5,7]))
print(solution(100,[1], [3,5,7]))