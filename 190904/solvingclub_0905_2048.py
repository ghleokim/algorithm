# def mergerow(row):
#     top = 0
#     for i in range(1, len(row)):
#         if row[i] and row[top] == row[i]:
#             row[top] *= 2
#             row[i] = 0
#             top = i
#         elif row[i] and row[top] != row[i]:
#             top = i
#     return row
"""
def mergerow(row, d):
    if d: # 거꾸로
        top = N-1
        for i in range(len(row)-2, -1, -1):
            if row[i]:
                if row[top] != row[i]: top = i
                else: row[top], row[i] = row[top] * 2, 0; top = i
    else: # 순방향
        top = 0
        for i in range(1,len(row)):
            if row[i]:
                if row[top] != row[i]: top = i
                else: row[top], row[i] = row[top] * 2, 0; top = i
    return row

def moverow(row, d):
    res = [0 for _ in range(N)]
    if d: # right
        i = N-1
        for r in row[::-1]:
            if r: res[i]=r;i -= 1
            
    else: # left
        i = 0
        for r in row:
            if r: res[i]=r; i += 1

    return res

# func test
# for i in range(4):
#     print(moverow((mergerow(A[i])),1))
# print()
# for i in range(4):
#     print(moverow((mergerow(A[i])),0))

for T in range(int(input())):
    N, D = input().split()
    N = int(N)
    dc={'up':0,'down':1,'left':0,'right':1}
    d=dc[D]
    D = 1 if D in 'updown' else 0

    board = [[*map(int,input().split())] for _ in range(N)]

    if D: board = [*zip(*board)]

    for i in range(N):
        board[i] = moverow((mergerow([*board[i]], d)),d)

    if D: board = [*zip(*board)]
    
    # print test
    # for i in range(N):
    #     print(' '.join(map(str,board[i])))
    # print(*[' '.join(map(str,board[i]))+'\n' for i in range(N)])

    print('#',end='')
    print(T+1,*[' '.join(map(str,board[i])) for i in range(N)], sep='\n')
"""
# shorten

def mg(w,d):
    if d:
        top=N-1
        for i in range(N-2,-1,-1):
            if w[i] and w[top]!=w[i]:top=i
            elif w[i]:w[top],w[i]=w[top]*2,0;top=i
    else:
        top=0
        for i in range(1,N):
            if w[i] and w[top]!=w[i]:top=i
            elif w[i]:w[top],w[i]=w[top]*2,0;top=i
    return w
def mv(w, d):
    z=[0]*N
    if d:
        i=N-1
        for r in w[::-1]:
            if r:z[i]=r;i-=1
    else:
        i=0
        for r in w:
            if r:z[i]=r;i+=1
    return z
for T in range(int(input())):
    N,D=input().split();N=int(N);dc={'up':0,'down':1,'left':0,'right':1};d=dc[D];D=1 if D in'updown'else 0;B=[[*map(int,input().split())]for _ in range(N)]
    if D:B=[*zip(*B)]
    for i in range(N):B[i]=mv((mg([*B[i]],d)),d)
    if D:B=[*zip(*B)]
    print(f'#',end='');print(T+1,*[' '.join(map(str,B[i]))for i in range(N)],sep='\n')


#minor change
def mg(w,d):
    if d:
        top=N-1
        for i in range(N-2,-1,-1):
            if w[i] and w[top]!=w[i]:top=i
            elif w[i]:w[top],w[i]=w[top]*2,0;top=i
    else:
        top=0
        for i in range(1,N):
            if w[i] and w[top]!=w[i]:top=i
            elif w[i]:w[top],w[i]=w[top]*2,0;top=i
    return w
def mv(w, d):
    z=[0]*N
    if d:
        i=N-1
        for r in w[::-1]:
            if r:z[i]=r;i-=1
    else:
        i=0
        for r in w:
            if r:z[i]=r;i+=1
    return z
for T in range(int(input())):
    N,D=input().split();N=int(N);dc={'up':0,'down':1,'left':0,'right':1};d=dc[D];D=1 if D in'updown'else 0;B=[[*map(int,input().split())]for _ in range(N)]
    if D:B=[*zip(*B)]
    for i in range(N):B[i]=mv((mg([*B[i]],d)),d)
    if D:B=[*zip(*B)]
    print(f'#{T+1}',end='');for i in range(N):print(*B[i])



"""
3
5 up
4 8 2 4 2
4 4 2 2 8
8 2 2 4 4
2 2 2 2 8
16 2 2 2 2
2 down
16 2
0 2
10 down
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4

"""