#   R       UP      L       DOWN
d = ((0,1), (-1,0), (0,-1), (1,0))

def check_boundary(N, nr, nc):
    return any([nr<0, nc<0, nr>N-1, nc>N-1])


def check_next(maze, r, c, direction):
    N = len(maze)
    dr = d[direction][0]
    dc = d[direction][1]
    nr = r + dr
    nc = c + dc
    
    if check_boundary(N,nr,nc):
        return False
    elif maze[nr][nc]:
        return False
    else:
        return True
    

def check_left(maze, r, c, direction):
    left_dir = (direction + 1) % 4

    dr = d[left_dir][0]
    dc = d[left_dir][1]

    N = len(maze)
    nr = r + dr
    nc = c + dc

    if check_boundary(N,nr,nc):
        return False
    
    elif maze[nr][nc]:
        return False
    
    return True

def move(maze, r, c, direction, count):
    if check_left(maze, r, c, direction) is True:
        direction = (direction + 1) % 4
        dr = d[direction][0]
        dc = d[direction][1]
        
        r += dr
        c += dc
        count += 1

    elif check_next(maze, r, c, direction) is True:
        dr = d[direction][0]
        dc = d[direction][1]
        
        r += dr
        c += dc
        count += 1

    else:
        direction = (direction - 1) % 4

    return r, c, direction, count


def solution(maze):
    N = len(maze)
    r = 0
    c = 0

    count = 0
    direction = 1

    while True:
        if r == N-1 and c == N-1:
            break
        
        r, c, direction, count = move(maze, r, c, direction, count)

    return count


print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))