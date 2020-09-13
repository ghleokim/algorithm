# keyIndex
"""
    keyIndex

    0 Enter
    1 move right
    2 move down
    3 move left
    4 move up
    5 ctrl right
    6 ctrl down
    7 ctrl left
    8 ctrl up

"""

from copy import deepcopy

direction = ((0,1), (1,0), (0,-1), (-1,0))

class Board:
    def __init__(self, board, r, c):
        self.board = [[*b] for b in board]
        self.r = r
        self.c = c
        self.count = 0
        self.selected = None
        self.history = [(r,c)]
        self.item_index = self.get_item_index(board)

    def get_item_index(self, board):
        item_index = [[] for _ in range(7)]
        for i in range(4):
            for j in range(4):
                if board[i][j]:
                    item_index[board[i][j]].append((i,j))
        return item_index

    def get_pair(self):
        r = self.selected[0]
        c = self.selected[1]
        if self.board[r][c]:
            for candi in self.item_index[self.board[r][c]]:
                if candi[0] == r and candi[1] == c: continue
                else:
                    return candi
        return False

    def __str__(self):
        return f"{self.count}"
    
    def cur_pos(self):
        return (self.r, self.c)

    def operate(self, keyIndex):
        self.count += 1
        if keyIndex == 0:
            # enter
            return self.enter()
        elif keyIndex < 5:
            # move
            return self.move(keyIndex)
        else:
            # ctrl
            return self.ctrl_move(keyIndex)

    def enter(self):
        if self.board[self.r][self.c] == 0:
            return False
        elif self.selected is None:
            self.selected = [self.r, self.c]
        else:
            selected_r = self.selected[0]
            selected_c = self.selected[1]
            
            if self.board[selected_r][selected_c] == self.board[self.r][self.c]:
                self.board[self.r][self.c] = 0
                self.board[selected_r][selected_c] = 0
                self.selected = None
                return True
            else:
                return False
        
        return True

    def move(self, keyIndex):
        keyIndex -= 1
        dr, dc = direction[keyIndex]
        nr = self.r+dr
        nc = self.c+dc

        if self.check_boundary(nr, nc):
            ###
            if (nr,nc) in self.history: return False
            
            self.history.append((nr,nc))
            ###

            self.r = nr
            self.c = nc
            return True
        else:
            return False
    
    def ctrl_move(self, keyIndex):
        keyIndex -= 5
        dr, dc = direction[keyIndex]
        
        nr = self.r + dr
        nc = self.c + dc

        if self.check_boundary(nr,nc):
            while self.check_boundary(nr, nc):
                if self.board[nr][nc]: break
                nr += dr
                nc += dc
            
            if self.check_boundary(nr,nc) is False:
                nr -= dr
                nc -= dc
            
            ###
            if (nr, nc) in self.history: return False
            self.history.append((nr,nc))
            ###

            self.r = nr
            self.c = nc
            return True
        else:
            return False

    def check_boundary(self, r, c):
        if any([r<0, c<0, r>3, c>3]): return False
        else: return True

    def check_board(self):
        for b in self.board:
            if sum(b) > 0: return False
        return True

def solution(board,r,c):
    answer = 0
    board_obj = Board(board, r, c)

    queue = [board_obj]

    while queue:
        prev_board = queue[0]
        print(prev_board.count)
        del queue[0]

        for i in range(9):
            cur_board = deepcopy(prev_board)

            if cur_board.selected:
                target_pair = cur_board.get_pair()

                dr = target_pair[0] - cur_board.r
                dc = target_pair[1] - cur_board.c

                d_candi = [0]

                if dc > 0:
                    d_candi.extend([1,5])
                elif dc < 0:
                    d_candi.extend([3,7])
                if dr > 0:
                    d_candi.extend([2,6])
                elif dr < 0:
                    d_candi.extend([4,8])

                if i not in d_candi:
                    continue

            result = cur_board.operate(i)
            if result is True:
                if cur_board.check_board() is True:
                    return cur_board.count
                queue.append(cur_board)
    
    return answer

res = solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1, 0)

# res = solution([[1,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]],0, 0)

# b = Board([[0,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0]],0,0)
# print(b.check_board())
print(res)

# b = Board([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],3, 0)

# print(b.operate(8))
# print(b.cur_pos())