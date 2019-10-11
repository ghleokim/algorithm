def getsum(node):
    if not tree[node]:
        if node*2+1 > N:
            tree[node]=getsum(node*2)
        else:
            tree[node]=getsum(node*2)+getsum(node*2+1)
        return tree[node]
    else:
        return tree[node]


for T in range(int(input())):
    N, M, L = map(int,input().split())
    tree = [0 for _ in range(N+1)]

    for i in range(M):
        n,v = map(int,input().split())
        tree[n] = v

    print('#',end='')
    print(T+1,getsum(L))

