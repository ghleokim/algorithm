is_finished = lambda n,pos: all([p == n for p in pos])
check_boundary = lambda n, pos: all([(p > 0 and p < n) for p in pos])

def can_move(board, posA, posB, dx, dy):
    n = len(board)

    nexA = [posA[0]+dy, posA[1]+dx]
    nexB = [posB[0]+dy, posB[1]+dx]

    boundary_check = [
        nexA[0] < 0, nexB[0] > n-1, 
        nexA[1] < 0, nexB[1] > n-1,
        nexB[0] < 0, nexB[0] > n-1,
        nexB[1] < 0, nexB[1] > n-1
    ]

    if any(boundary_check):
        print('boundary')
        return False
    
    board_check = [
        board[nexA[0]][nexA[1]],
        board[nexB[0]][nexB[1]]
    ]
    
    if any(board_check):
        print(board_check, nexA, nexB)
        return False

    return True

def rotate_if_can(board, posA, posB, direction, pivot):
    n = len(board)

    pivot_index = ((0,1),(1,0),(0,-1),(-1,0)) #((1,0), (0,1), (-1,0), (0,-1))
    if pivot == 0:
        pivot_index = pivot_index[::direction]
        posB_direction = [posB[i]-posA[i] for i in range(2)]
        
        for j in range(4):
            if posB_direction[0] == pivot_index[j][0] and posB_direction[1] == pivot_index[j][1]:
                break
        
        next_direction = pivot_index[(j + 1) % 4]
        nextB = [posA[i]+next_direction[i] for i in range(2)]

        boundary_check = [
            nextB[0] < 0, nextB[0] > n-1,
            nextB[1] < 0, nextB[1] > n-1
        ]

        if any(boundary_check):
            return None
        
        rotation_check = (
            posA[0]+next_direction[0]+posB_direction[0],
            posA[1]+next_direction[1]+posB_direction[1]
        )
        
        if board[rotation_check[0]][rotation_check[1]]:
            return None
        elif board[nextB[0]][nextB[1]] == 0:
            return (posA, tuple(nextB))
        else:
            return None

    else:
        pivot_index = pivot_index[::direction]
        posA_direction = [posA[i]-posB[i] for i in range(2)]

        for j in range(4):
            if posA_direction[0] == pivot_index[j][0] and posA_direction[1] == pivot_index[j][1]:
                break
        
        next_direction = pivot_index[(j + 1) % 4]
        nextA = [posB[i]+next_direction[i] for i in range(2)]

        boundary_check = [
            nextA[0] < 0, nextA[0] > n-1,
            nextA[1] < 0, nextA[1] > n-1,
        ]

        if any(boundary_check):
            return None
        
        rotation_check = (
            posB[0]+next_direction[0]+posA_direction[0],
            posB[1]+next_direction[1]+posA_direction[1]
        )
        
        if board[rotation_check[0]][rotation_check[1]]:
            return None
        elif board[nextA[1]][nextA[0]] == 0:
            return (tuple(nextA), posB)
        else:
            return None

print(is_finished(3,(3,3)))

def solution(board):
    answer = 0

    time = 0
    posA = (0,0)
    posB = (1,0)
    former_list = []

    queue = [[time, posA, posB, former_list]]

    while queue:
        print(queue[0])
        time, posA, posB, former_list = queue[0]
        del queue[0]

        if is_finished(len(board), posA) or is_finished(len(board), posB):
            answer = time
            break

        # move up down right left
        for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)): # 상하좌우
            if can_move(board, posA, posB, dx, dy):
                posA = (posA[0]+dy, posA[1]+dx)
                posB = (posB[0]+dy, posB[1]+dx)

                if (posA, posB) in former_list:
                    continue

                new_former_list = former_list + [(posA, posB)]

                next_item = [time+1, posA, posB, new_former_list]
                queue.append(next_item)
        # rotate    
        for direction, pivot in ((-1,0),(-1,1),(1,0),(1,1)):
            rotate_res = rotate_if_can(board, posA, posB, direction, pivot)
            if rotate_res == None: continue
            
            posA, posB = rotate_res

            if (posA, posB) in former_list:
                continue

            new_former_list = former_list + [(posA, posB)]

            next_item = [time+1, posA, posB, new_former_list]
            queue.append(next_item)

    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

# print(rotate_if_can(
#     [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]],
#     (0,2),
#     (0,1),
#     1,1
#     ))

# print(can_move(
#     [[0, 0, 0, 1, 1],
#     [0, 0, 0, 1, 0],
#     [0, 1, 0, 1, 1],
#     [1, 1, 0, 0, 1],
#     [0, 0, 0, 0, 0]],
#     (2,1),
#     (2,2),
#     0,1
# ))
