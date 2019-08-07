# electricBus
for t in range(int(input())):
    (k, n, m), stops = (map(int, input().split()), list(map(int, input().split())))
    road = list(range(n+1))
    index = 0
    count = 0
    notFound = False
    while index + k < n:
        reach = road[index+1:index+k+1]
        for position in reach[::-1]:
            if position in stops:
                index = position
                count += 1
                break
            else:
                continue
        else:
            notFound = True
        if notFound:
            count = 0
            break
        
    print('#{0} {1}'.format(t + 1, count))