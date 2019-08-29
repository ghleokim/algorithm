
# front, rear index 조작

for T in range(int(input())):
    N, M = map(int, input().split())
    Q = [*map(int,input().split())]
    while M >= N:
        M = M % N
    print('#{0} {1}'.format(T+1,Q[M]))