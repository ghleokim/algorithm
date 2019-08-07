# 1. without modules
for t in range(int(input())):
    n, inp = (int(input()), input())
    ref = [0] * 10
    #count 0~9 in a list: ref
    for idx in range(n):
        ref[int(inp[idx])] += 1
    res = [0, 0]
    for e, value in enumerate(ref):
        if value >= res[1]:
            res[0] = e
            res[1] = value
    print('#{0} {1} {2}'.format(t+1, res[0], res[1]))

# 2. with modules and builtin functions
# https://www.quora.com/How-do-I-find-the-most-repeated-integer-in-a-list-in-python
for t in range(int(input())):
    n, i = (int(input()), list(map(int,list(input()))))
    k = max(sorted(i)[::-1], key=i.count)
    print(f'#{t+1} {k} {i.count(k)}')
