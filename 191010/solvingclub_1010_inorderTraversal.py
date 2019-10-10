"""
def inorder(res,node=1):
    global length
    if node > length-1: return
    elif not tree[node]: return
    else:
        inorder(res,node*2)
        res.append(tree[node])
        inorder(res,node*2+1)

for T in range(10):
    N = int(input())
    length = 1

    while length < N:
        length*=2
    length += 1

    tree = [None for _ in range(length)]

    for i in range(N):
        info = input().split()
        tree[int(info[0])] = info[1]

    res = []
    inorder(res)

    print('#',end='')
    print(T+1,''.join(res))
"""
"""
def inorder2(node=1):
    global length, res
    if node > length-1: return
    elif not tree[node]: return
    else:
        inorder2(node*2)
        if node < 10:
            res += tree[node][2]
        elif node < 100:
            res += tree[node][3]
        else:
            res += tree[node][4]
        inorder2(node*2+1)

for T in range(1):
    N = int(input())
    length = 1

    while length < N:
        length <<= 1
    length += 1

    tree = [0]+[input() for _ in range(N)]+[0 for _ in range(length-N-1)]
    print(len(tree), tree)
    res = ''
    inorder2()

    print('#',end='')
    print(T+1,res)
"""
"""181ms
def inorder(res,node=1):
    global length, top
    if node > N: return
    elif not tree[node-1]: return
    else:
        inorder(res,node*2)
        if node < 10:
            res[top] = tree[node-1][2]
        elif node < 100:
            res[top] = tree[node-1][3]
        else:
            res[top] = tree[node-1][4]
        top += 1
        inorder(res,node*2+1)

for T in range(10):
    N = int(input())
    length = 1

    while length < N:
        length*=2
    length += 1

    tree = [input() for _ in range(N)]

    top=0
    res = [None for i in range(N)]
    inorder(res)

    print('#',end='')
    print(T+1,''.join(res))
"""

def getinorder(order,node=1):
    left=node*2
    right=left+1

    if left < N+1: getinorder(order,left)
    order.append(node)
    if right < N+1: getinorder(order,right)

# print(dir(list()))

for T in range(1):
    N = int(input())
    length = 1
    while length < N:
        length*=2
    length += 1
    order=[]
    getinorder(order)
    tree = [input().split() for _ in range(N)]
    
    print(order)

    print('#',end='')
    print(T+1,''.join([tree[i-1][1] for i in order]))
    
    
    # tree = [input().split() for _ in range(N)]
    # top=0
    # res = [None for i in range(N)]

    # print('#',end='')
    # print(T+1,''.join(res))