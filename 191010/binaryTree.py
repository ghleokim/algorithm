tree = "1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13"

def binaryTree(parent, child):
    if not treeList[1]:
        treeList[1] = parent
        treeList[2] = child
    else:
        for node, value in enumerate(treeList):
            if value == parent:
                break
        if node*2 > len(treeList) - 2:
            treeList.extend([None for _ in range(len(treeList)-1)])
            print(treeList)
        if not treeList[node*2]:
            treeList[node*2] = child
            return
        elif not treeList[node*2+1]:
            treeList[node*2+1] = child
            return


treeinput = [*map(int, tree.split())]

num = 3

treeList = [None for i in range(num)]

for i in range(len(treeinput)//2):
    print(treeinput[2*i], treeinput[2*i+1])
    binaryTree(treeinput[2*i], treeinput[2*i+1])

print(treeList)


def preorder(node=1, depth=0):
    if node > len(treeList)-1: return
    elif not treeList[node]: return
    else:
        print('node', node, 'depth', depth, 'value', treeList[node])
        preorder(node*2, depth+1)
        preorder(node*2+1, depth+1)

print('preorder traversal')
preorder()

def inorder(node=1):
    if node > len(treeList)-1: return
    elif not treeList[node]: return
    else:
        inorder(node*2)
        print('node', node, 'value', treeList[node])
        inorder(node*2+1)

print('inorder traversal')
inorder()

def postorder(node=1):
    if node > len(treeList)-1: return
    elif not treeList[node]: return
    else:
        postorder(node*2)
        postorder(node*2+1)
        print('node', node, 'value', treeList[node])

print('postorder traversal')
postorder()