# 부모 노드를 찾는 것
def findset(x):
    t = x
    while t != D[t]:
        t = D[t]
    return t

# 1부터 N까지 initialize
def makeset(N):
    return [i for i in range(N+1)]

# 
def union(x,y):
    D[findset(x)] = y

for T in range(int(input())):
    N, M = map(int,input().split())
    paper = [*map(int,input().split())]
    paper2 = set((min(paper[2*i], paper[2*i+1]),max(paper[2*i], paper[2*i+1])) for i in range(M))

    paper2 = sorted(list(paper2))
    print(paper2)

    D = makeset(N)

    for p, q in paper2:
        union(p,q)
    
    print([findset(l) for l in range(1,N+1)])

    print('#',end='')
    print(T+1, len(set(findset(l) for l in range(1,N+1))))