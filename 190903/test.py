import random

N = 1000

with open('input.txt', 'w') as f:
    f.write('1\n')
    f.write(str(N)+' '+str(N)+'\n')
    for i in range(N):
       f.write(' '.join(map(str,random.choices(range(1000),k=N))))
       f.write('\n')