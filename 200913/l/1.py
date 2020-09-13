def put(inventory, box, answer, num_boxes):
    for i in box:
        if inventory[i]:
            answer -= 1
            num_boxes -= 1
        else:
            inventory[i] += 1
            answer += 1
    return answer, num_boxes

def solution(boxes):
    inventory = [0 for _ in range(1000001)]

    answer = 0
    num_boxes = len(boxes)

    for box in boxes:
        answer, num_boxes = put(inventory, box, answer, num_boxes)
    
    return min(answer, num_boxes)

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))