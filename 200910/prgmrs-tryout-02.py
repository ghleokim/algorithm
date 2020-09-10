def check_boundary(n, nr, nc):
    if any((nr < 0, nr > n-1, nc < 0, nc > n-1)):
        return False
    return True

def check_next(board, nr, nc):
    if board[nr][nc] != 0:
        return False
    return True

def solution(n):
    max_number = n ** 2 - sum([i for i in range(n)])

    answer = []

    directions = ((1,0), (0,1), (-1,-1))

    board = [[0 for _ in range(n)] for __ in range(n)]

    d_index = 0
    r = 0
    c = 0
    cur_number = 1 

    while cur_number <= max_number:
        board[r][c] = cur_number

        dr, dc = directions[d_index]
        nr = r+dr
        nc = c+dc


        if not check_boundary(n, nr, nc) or not check_next(board, nr, nc):
            d_index = (d_index + 1) % 3
            dr, dc = directions[d_index]    
        
        cur_number += 1
        r += dr
        c += dc

    for bo in board:
        for b in bo:
            if b != 0:
                answer.append(b)
        

    return answer


solution(4)
solution(5)
solution(6)