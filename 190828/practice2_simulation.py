def isEmpty():
    if rear == -1: return True
    return False

queue = [0 for _ in range(20)]
front, rear = -1, -1

person = 0
candy = 20

input()
person += 1
rear += 1; queue[rear] = (person, 0)

while candy:
    print('#',person)
    print('candy', candy)
    print(queue)
    print('current queue ', queue[front+1:rear+1])
    print('front, rear: ', front, rear)
    tmp = rear
    tf, tr = -1, -1

    while front != rear:
        # deQueue()
        front += 1; p, c = queue[front]; queue[front] = 0
        # candy+1
        c += 1; candy -= 1
        # enQueue()
        tmp += 1; queue[tmp] = (p, c)
    
    print('next: ', queue)
    front, rear = rear, tmp
    person += 1
    rear += 1; queue[rear] = (person, 0)
    input()
