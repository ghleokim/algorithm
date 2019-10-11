"""
char ord
+    43
-    45
*    42
/    47

"""
"""
def arith(L,R,OP):
    op=ord(OP)
    if op == 43: return L+R
    elif op == 45: return L-R
    elif op == 42: return L*R
    else: return L//R

def postorder(node=1):
    if len(tree[node])==2: return int(tree[node][1])
    else:
        L = postorder(int(tree[node][2]))
        R = postorder(int(tree[node][3]))
        return arith(L,R,tree[node][1])

# row = node op node node
# row = node num

for T in range(10):
    N = int(input())
    tree = [0 for _ in range(N+1)]

    for i in range(1,N+1):
        tree[i] = input().split()

    print('#',end='')
    print(T+1,postorder())

"""

# ----------------------------------- #

ar=lambda L,R,OP:L+R if ord(OP)==43 else L-R if ord(OP)==45 else L*R if ord(OP)==42 else L//R
def po(n):return int(n[1])if len(n)==2 else ar(po(tr[int(n[2])]),po(tr[int(n[3])]),n[1])
for T in range(10):N=int(input());tr=[0]+[input().split()for _ in range(N)];print('#',end='');print(T+1,po(tr[1]))