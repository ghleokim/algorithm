def amp(p, i=1):
    while p > i: p -= i; i += 1
    return((p,i-p+1))

def add(c):
    (x,y),(z,w)=c
    return ((x+z,y+w))

def sharp(x,y):
    return (x+y-1)*(x+y-2)//2+x
    return sum([i for i in range(x+y-1)])+x
    # sum([i for i in range(x+y-1)])+x

for T in range(int(input())):
    print('#',end='');print(T+1,sharp(*add([*map(amp,map(int,input().split()))])))

