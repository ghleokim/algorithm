def rotate(B):
    NB = [row[::-1] for row in [*zip(*B)]]
    return NB

def myJoin(S):
    return ''.join([*map(str,S)])

for T in range(int(input())):
    N = int(input())
    B = [[*map(int,input().split())] for _ in range(N)]
    B1 = rotate(B); B2 = rotate(B1); B3 = rotate(B2)
    
    print('#{}'.format(T+1), end=' ')
    for i in range(N):
        print(*map(myJoin,(B1[i],B2[i],B3[i])))
