for T in range(int(input())):
    D, M, Q, Y = map(int,input().split())
    P = [*map(int,input().split())]

    months = [min(M, D*p) for p in P]
    months.extend([0,0,0])

    i=11
    while i !=- 1:
        months[i] = min(months[i]+months[i+1], Q+months[i+3])
        i -= 1

    # months[-1] = min(months[-1], Q)
    # for i in range(10,-1,-1):
    #     if i > 8: months[i] = min(months[i]+months[i+1], Q)
    #     else: months[i] = min(months[i]+months[i+1], Q+months[i+3])

    ans = min(Y, months[0])

    print('#',end='')
    print(T+1,ans)

# short ------------- #
for T in range(int(input())):
 D,M,Q,Y=map(int,input().split())
 P,i=[*map(int,input().split())],11
 m=[min(M,D*p)for p in P]+[0]*3
 while i!=-1:m[i]=min(m[i]+m[i+1],Q+m[i+3]);i-=1
 a=min(Y,m[0])
 print(f'#{T+1} {a}')
 print('#',end='');print(T+1,a)


# shorter ----------- #
u=input;n=min;q=lambda:map(int,u().split())
for T in range(int(u())):
 D,M,Q,Y=q();P,i=[*q()],11;m=[n(M,D*p)for p in P]+[0]*3
 while i>-1:m[i]=n(m[i]+m[i+1],Q+m[i+3]);i-=1
 print(f'#{T+1} {n(Y,m[0])}')

u=input;n=min;q=lambda:map(int,u().split())
for T in range(int(u())):
 D,M,Q,Y=q();P,i=[*q()],11;m=[n(M,D*p)for p in P]+[0]*3
 while i>-1:m[i]=n(m[i]+m[i+1],Q+m[i+3]);i-=1;;print(f'#{T+1} {n(Y,m[0])}')

