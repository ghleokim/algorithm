Z = [0 for _ in range(10)]
O = [1 for _ in range(10)]
print((lambda x,y: Z[:x]+O[x:y+1]+Z[y+1:])(*map(int,input().split())))