def chk(S):return 1 if len(S)==len(set(S)) else 0
# 4 more shorten
for T in range(int(input())):
    A,B=input(),'SDHC';r={z:{*range(1,14)}for z in B};print('#{0}'.format(T+1),end=' ')
    D=[(A[i*3],int(A[i*3+1:i*3+3])) for i in range(len(A)//3)]
    if chk(D):
        for d in D:
            r[d[0]]=dif(*d)
    
    print(*map(len,[r[z]for z in B])
    