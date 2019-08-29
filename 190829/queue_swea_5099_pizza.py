import time
# 원형 큐

for T in range(int(input())):
    N, M = map(int, input().split())
    P = [*map(int,input().split())]
    nP = 0

    N += 1

    Q = [0 for _ in range(N)]
    front = 0
    rear = 0

    rear += 1
    Q[rear] = (nP, P[nP])
    nP += 1

    while front != rear:
        # time.sleep(0.3)
        # print(Q, front, rear)
        # 포화
        if (rear+1)%N == front:
            # dequeue / calc / enqueue
            front+=1
            front%=N
            i, cur = Q[front]
            cur //= 2
            Q[front] = 0
            if cur:
                rear+=1
                rear%=N
                Q[rear] = (i, cur)
        # 여유: 큐 추가, 추가할 것이 없으면 
        else:
            # if pizza left: add pizza
            if nP < M:
                rear+=1
                rear%=N
                Q[rear] = (nP, P[nP])
                nP+=1
            else:
                # dequeue / calc / enqueue
                front+=1
                front%=N
                i, cur = Q[front]
                cur //= 2
                Q[front] = 0
                if cur:
                    rear+=1
                    rear%=N
                    Q[rear] = (i, cur)

    print('#',end='');print(T+1,i+1)






"""
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2


# 화덕이 비어있지 않은 동안 반복
while Q[(front+1)%(N+1)]:
    time.sleep(1)
    print(Q, front, rear)
    # 포화
    if (rear + 1) % (N+1) == front:
        # check next pizza
        front = (front+1) % (N+1)
        if not Q[front]:
            if nP<M:
                rear = (rear+1) % (N+1)
                Q[rear] = P[nP]
                nP += 1
        # if next pizza
        else:
            # dequeue
            cur = Q[front]
            Q[front] = 0
            cur = cur // 2
            if cur:
                rear = (rear+1) % (N+1)
                Q[rear] = cur
            else:
                if nP<M:
                    rear = (rear+1) % (N+1)
                    Q[rear] = P[nP]
                    nP += 1  
    # 여유
    else:
        if not Q[front]:
            if nP < M:
                rear = (rear+1) % (N+1)
                Q[rear] = P[nP]
                nP += 1
            else:
                rear = (rear+1) % (N+1) 
        else:
            cur = Q[front]
            cur //= 2
            if cur:
                rear = (rear+1) % (N+1)
                Q[rear] = cur
"""