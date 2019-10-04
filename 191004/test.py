for T in range(int(input())):
 D,M,Q,Y=map(int,input().split())
 P,i=[*map(int,input().split())],11
 m=[min(M,D*p)for p in P]+[0]*3
 while i!=-1:m[i]=min(m[i]+m[i+1],Q+m[i+3]);i-=1
 a=min(Y,m[0])
 print('#',end='');print(T+1,a)