is_finished = lambda n,pos: all([p == n-1 for p in pos])
board_is_empty = lambda board,nr,nc: not board[nr][nc]

def check_visited(visited, A, B):
    cur_direction = (B[0]-A[0],B[1]-A[1])
    rotation_direction = ((0,1),(1,0),(0,-1),(-1,0))
    i = 0
    while i < 4:
        if cur_direction == rotation_direction[i]:
            break
        i += 1

    if visited[A[0]][A[1]] & (1 << i):
        return True

    return False

def visit(visited, A, B):
    cur_direction = (B[0]-A[0],B[1]-A[1])
    rotation_direction = ((0,1),(1,0),(0,-1),(-1,0))
    i = 0
    while i < 4:
        if cur_direction == rotation_direction[i]:
            break
        i += 1

    visited[A[0]][A[1]] += 1 << i
    visited[B[0]][B[1]] += 1 << ((i+2)%4)

    return

def check_boundary(n, nr, nc):
    return not any((
        nr < 0, nc < 0,
        nr > n-1, nc > n-1
    ))

def check_boundary_list(n, n_list):
    n_list_check = [any([i<0, i>n-1]) for i in n_list]
    return not any(n_list_check)

def translate(board, A, B, dr, dc):
    n = len(board)
    nextAr = A[0]+dr
    nextAc = A[1]+dc
    nextBr = B[0]+dr
    nextBc = B[1]+dc

    if check_boundary_list(n, [nextAc, nextAr, nextBc, nextBr]) and all([
        board_is_empty(board,nextAr,nextAc), board_is_empty(board,nextBr,nextBc)
    ]):
        return [[nextAr, nextAc], [nextBr, nextBc]]
        
    else:
        return None

def rotate(board, A, B, direction): # change A and B on input
    n = len(board)

    rotation_direction = ((0,1),(1,0),(0,-1),(-1,0))
    rotation_direction = rotation_direction[::direction]
    cur_direction = (B[0]-A[0], B[1]-A[1])

    i = 0
    while i < 4:
        if cur_direction == rotation_direction[i]:
            next_direction = rotation_direction[(i + 1) % 4]
            break
        i += 1

    nextBr = A[0]+next_direction[0]
    nextBc = A[1]+next_direction[1]
    checkBr = A[0]+cur_direction[0]+next_direction[0]
    checkBc = A[1]+cur_direction[1]+next_direction[1]
    
    if check_boundary_list(n, [nextBc, nextBr, checkBc, checkBr]) and all([
        board_is_empty(board,nextBr,nextBc), board_is_empty(board,checkBr,checkBc)
    ]):
        return [A, [nextBr, nextBc]]
    else:
        return None


def solution(board):
    answer = 0
    n = len(board)
    time = 0
    A = [0,0]
    B = [0,1]
    visited = [[0 for _ in range(n)] for __ in range(n)]

    visit(visited, A, B)

    queue = [[time, A, B, [*visited]]]

    while queue:
        time, A,B, cur_visited = queue[0]
        print(queue[0])
        del queue[0]

        if is_finished(n, A) or is_finished(n, B):
            answer = time
            break
        
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            t_result = translate(board, A, B, dr, dc)
            if t_result == None: continue

            nA, nB = t_result
            if check_visited(cur_visited, nA, nB): continue

            next_visited = [*cur_visited]
            visit(next_visited, nA, nB)
            queue.append([time+1, nA, nB, next_visited])

        for dd in (-1,1):
            r_result = rotate(board, A, B, dd)
            if r_result != None:
                nA, nB = r_result
                if not check_visited(cur_visited, nA, nB):    
                    next_visited = [*cur_visited]
                    visit(next_visited, nA, nB)
                    queue.append([time+1, nA, nB, next_visited])

            r_result = rotate(board, B, A, dd)
            if r_result != None:
                nB, nA = r_result
                if not check_visited(cur_visited, nA, nB):
                    next_visited = [*cur_visited]
                    visit(next_visited, nA, nB)
                    queue.append([time+1, nA, nB, next_visited])

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
