"""
char ord
+    43
-    45
*    42
/    47
"""

def arith(L,R,OP):
    op = ord(OP)
    if op == 43: return L+R
    elif op == 45: return L-R
    elif op == 42: return L*R
    else: return L//R


def postorder(node=1):
    if node > length: return None
    elif tree[node][1].isdigit

    L = postorder(node*2)
    R = postorder(node*2+1)
    return arith(L,R,tree[node][1])


for 