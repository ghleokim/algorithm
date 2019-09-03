for T in range(int(input())):   
    N, M, L = map(int,input().split())

    num = input().split()

    for i in range(M):
        dest, value = map(int,input().split())
        num = [*num[0:dest],value,*num[dest:]]

    print('#',end='')
    print(T+1, num[L])