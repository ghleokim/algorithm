def inorder(node=1):
    global count
    if node > N: return
    elif not tree[node]: return
    else:
        inorder(node*2)
        count += 1
        if node == 1: res[0] = count
        elif node == N//2: res[1] = count
        inorder(node*2+1)

for T in range(int(input())):
    res = [0,0]
    N = int(input())
    tree = [i for i in range(N+1)]
    count = 0
    inorder()
    print('#',end='')
    print(T+1,*res)