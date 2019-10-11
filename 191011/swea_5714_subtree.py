def subtree(node):
    if not tree[node]: return
    else:
        global count
        count += len(tree[node])
        for n in tree[node]:
            subtree(n)

for T in range(int(input())):
    E, N = map(int,input().split())
    tree = [0 for _ in range(E+2)]
    lines = [*map(int,input().split())]
    for i in range(E):
        if tree[lines[2*i]]: tree[lines[2*i]].append(lines[2*i+1])
        else:
            tree[lines[2*i]] = [lines[2*i+1]]
    count = 1
    subtree(N)
    
    print('#',end='')
    print(T+1,count)