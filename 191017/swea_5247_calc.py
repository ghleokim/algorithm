def f(l):
    res = []
    for t in (l-1, l+1, l*2, l-10):
        if 0 < t <= 10 ** 6:
            res.append(t)
    return res

for T in range(int(input())):
    N, M = map(int,input().split())
    num = [-1 for _ in range(10**6+1)]

    num[N] = 0
    count = 0
    former = None

    while num[M]==-1:
        count += 1
        #something
        if former is None:
            former = f(N)
            for n in former:
                num[n] = count
        else:
            former = list(set(i for sub in [f(j) for j in former] for i in sub))
            newformer = []
            for n in former:
                if num[n] < 0:
                    num[n] = count
                    newformer.append(n)
            former = newformer

    print('#',end='')
    print(T+1,num[M])
