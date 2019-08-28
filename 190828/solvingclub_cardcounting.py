# A, 2 ~ 10, J, Q, K

# 1 using set
def diff(a,b):
    # a: set | b: int
    # returns set a without b if changed, None if not changed
    tmp = a.difference({b})
    if a != tmp: return tmp

for T in range(int(input())):
    TC = input()
    print('#{0}'.format(T+1), end=' ')
    ref = {}
    ref['D'] = ref['H'] = ref['C'] = ref['S'] = {k for k in range(1,14)}

    # print(ref)

    for i in range(len(TC)//3):
        card = TC[i * 3]
        num = TC[i * 3 + 1:(i + 1) * 3]
        # print(card)
        temp = diff(ref[card],int(num))
        if temp is None:
            print('ERROR')
            break
        ref[card] = temp
    else:
        print(*map(len,(ref['S'],ref['D'],ref['H'],ref['C'])))

# 2 shorten
for T in range(int(input())):
    A,B=input(),'SDHC';r={z:{*range(1,14)}for z in B};print('#{0}'.format(T+1),end=' ')
    for i in range(len(A)//3):
        j=i*3;c,n=A[j],A[j+1:j+3];t=r[c].difference({int(n)})
        if r[c]==t:print('ERROR');break
        r[c]=t
    else:print(*map(len,[r[z]for z in B]))

# 3
for T in range(int(input())):
    # A : input string, B: card type
    A, B=input(), 'SDHC'
    # r: dictionary for each card - [str|type]:[set|{1,...,13}]
    r = { z : {*range(1,14)} for z in B }
    print('#{0}'.format(T+1),end=' ')
    for i in range(len(A)//3):
        # j : index for each case
        j=i*3
        # c : card type, n: number
        c, n = A[j], A[j+1:j+3]
        # t = tmp for checking difference
        t = r[c].difference({int(n)})
        # if not changed exit and print error
        if r[c] == t: print('ERROR'); break
        # update dictionary
        r[c]=t
    else:
        # if no collapsing print result
        print(*map(len,[r[z] for z in B]))


# 4 more shorten
def f(c,n):r[c]=r[c].difference({n})
for T in range(int(input())):A,B=input(),'SDHC';r={z:{*range(1,14)}for z in B};print('#{0}'.format(T+1),end=' ');D=[(A[i*3],int(A[i*3+1:i*3+3]))for i in range(len(A)//3)];print(*map(len,[r[z]for z in B]))if [f(*d)for d in D if len(D)==len(set(D))]else print('ERROR')


"""
3
S01D02H03H04
H02H10S11H02
S10D10H10C01

"""
