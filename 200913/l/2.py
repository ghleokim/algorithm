def solution(ball, order):
    answer = []

    stale = [0 for _ in range(300001)]

    front = 0
    back = len(ball)-1

    order_index = 0

    while front <= back:
        if front == back:
            answer.append(ball[front])
            break
        
        target = order[order_index]

        if ball[front] == target:
            answer.append(ball[front])
            front += 1
        elif ball[back] == target:
            answer.append(ball[back])
            back -= 1
        else:
            stale[target] += 1
            order_index += 1

        # stale check
        while stale[ball[front]]:
            answer.append(ball[front])
            front += 1

        while stale[ball[back]]:
            answer.append(ball[back])
            back -= 1

    return answer

print(solution([1, 2, 3, 4, 5, 6],	[6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24],	[9, 2, 13, 24, 11]))
