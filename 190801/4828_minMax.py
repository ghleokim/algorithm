# minMax problem

# bubble sort
for t in range(int(input())):
    n, a = (int(input()), list(map(int,input().split())))

    for i in range(len(a)-1, -1, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    
    res = a[-1] - a[0]

    print('#{0} {1}'.format(t+1, res))
