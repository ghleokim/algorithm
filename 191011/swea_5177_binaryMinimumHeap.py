def heapadd(v):
    heaptree.append(v)
    child = len(heaptree)-1
    parent = child // 2
    # print(value, parent, child, heaptree)

    while heaptree[child] < heaptree[parent] and child != 1:
        temp = heaptree[child]
        heaptree[child] = heaptree[parent]
        heaptree[parent] = temp

        temp = parent
        parent = child // 2
        child = temp


        # heaptree[child], heaptree[parent] = heaptree[parent], heaptree[child]
        # parent, child = child//2, parent
        # print(value, parent, child, heaptree)
        # if child == 1: return

for T in range(int(input())):
    N = int(input())
    heaptree = [0]
    treelist = [*map(int,input().split())]

    for t in treelist: heapadd(t)

    lastnode = N
    result = 0

    while lastnode != 1:
        lastnode //= 2
        result += heaptree[lastnode]

    print('#', end='')
    print(T+1,result)


    