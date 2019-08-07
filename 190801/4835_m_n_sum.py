# 1. without modules
for t in range(int(input())):
    (n, m), a = (map(int, input().split()), list(map(int, input().split())))

    res = [0] * (n-m+1)

    for e, r in enumerate(res):
        for num in a[e:e+m]:
            r += num
        res[e] = r

    # sort res

    for i in range(len(res), -1, -1):
        for j in range(i-1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    
    print('#{0} {1}'.format(t+1, res[-1]-res[0]))

# 2. with modules
for t in range(int(input())):
    (n, m), a, d= (map(int, input().split()), list(map(int, input().split())), [])
    for e in range(n-m+1):
        d.append(sum(a[e:e+m]))
    print('#{0} {1}'.format(t+1,max(d)-min(d)))