"""
for T in range(int(input())):
    bus = [0 for _ in range(5001)]
    N = int(input())
    for i in range(N):
        a,b=map(int,input().split())
        for j in range(a,b+1):
            bus[j] += 1

    idx = []
    for i in range(int(input())):
        idx.append(int(input()))
    
    res = [*map(lambda x: str(bus[x]), idx)]

    print('#',end='')
    print(T+1,' '.join(res))
"""
"""
# basic methods shorten
for T in range(int(input())):
    N = int(input())
    B = [(lambda x, y: [0]*x+[1]*(y-x+1)+[0]*(10-y))(*map(int,input().split())) for i in range(N)]

    # for i in range(int(input())):
    #     s,e=map(int,input().split())
    #     for j in range(s,e+1):B[j]+=1
    k = [int(input()) for _ in range(int(input()))]
    print('#',end='');print(T+1,' '.join([*map(lambda x:str(B[x]),k)]))
"""
"""
#list slicing

for T in range(int(input())):
    N = int(input())
    bus = [0 for _ in range(N)]
    for i in range(N):
        s,e = map(int,input().split())
        bus[i] = [0]*s+[1]*(e-s+1)+[0]*(10-e)
    k = []
    for i in range(int(input())): k.append(int(input()))
    print(' '.join([str(sum([*zip(*bus)][i]))for i in k]))
"""

# shorten
for T in range(int(input())):
    Z = [0 for _ in range(5001)]
    O = [1 for _ in range(5001)]
    B = [(lambda x,y: Z[:x]+O[x:y+1]+Z[y+1:])(*map(int,input().split())) for i in range(int(input()))]
    k = [int(input()) for i in range(int(input()))]
    print('#',end='');print(T+1,*[sum([*zip(*B)][i]) for i in k])


"""
1
2
1 3
2 5
5
1
2
3
4
5

"""