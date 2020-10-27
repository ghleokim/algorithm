# turn : fish move 1 ~ 15, shark move case 1 2 3 4...
example = """7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2"""

print_strings = ['','↑', '↖', '←', '↙', '↓', '↘', '→', '↗']

class Board:
    direction = (
                ( 0, 0), #  none
                (-1, 0), # ↑
                (-1,-1),  # ↖
                ( 0,-1), # ←
                ( 1,-1), # ↙
                ( 1, 0), # ↓
                ( 1, 1), # ↘
                ( 0, 1), # →
                (-1, 1)  # ↗
                )

    def __init__(self, board, fishes):
        self.board = [[[board[i][j][k] for k in range(2)] for j in range(4)] for i in range(4)]
        self.fishes = [[*fishes[l]] for l in range(17)]

        # set shark at 0,0
        self.shark = [0,0]
        self.score = board[0][0][0]
        self.board[0][0][0] = -1

        self.fishes[self.score] = []

        # print(self.direction)
        # print(self.direction[self.get_shark_dir()])

    def get_shark_dir(self):
        shark_r = self.shark[0]
        shark_c = self.shark[1]
        shark_dir = board[shark_r][shark_c][1]
        return shark_dir
    
    def get_shark_candidate(self):
        if self.shark:
            
        else:
            return None
    
    def can_move(self, r, c, dr, dc, shark=False):
        if dr == 0 and dc == 0:
            return False
        elif any((r+dr > 3, c+dc > 3, r+dr < 0, c+dc < 0)):
            return False
        elif self.board[r+dr][c+dc][0] == -1:
            return False # shark
        return True
    
    def move(self, fish_number=-1, shark=False, destination=[-1,-1]):
        if fish_number == -1 and not shark:
            return None
        elif fish_number > 0:
            if len(self.fishes[fish_number]) == 0:
                return None
            fish_r = self.fishes[fish_number][0]
            fish_c = self.fishes[fish_number][1]
            fish_dir = self.fishes[fish_number][2]
            print(self.fishes)
            if fish_dir == -1:
                return None
            
            # check direction, set direction
            can_move = False
            while not can_move:
                dr = self.direction[fish_dir][0]
                dc = self.direction[fish_dir][1]
                can_move = self.can_move(fish_r, fish_c, dr, dc)
                print(f'      {fish_number} can/cannot move :', can_move)
                if not can_move:
                    fish_dir = (fish_dir+1) % 9
                    if fish_dir == 0: fish_dir += 1
            
            dr = self.direction[fish_dir][0]
            dc = self.direction[fish_dir][1]
            self.board[fish_r][fish_c][1] = fish_dir
            fish_nr = fish_r + dr
            fish_nc = fish_c + dc

            # change fishes
            change_fish = self.board[fish_nr][fish_nc][0]
            
            self.fishes[fish_number][0], self.fishes[change_fish][0] = self.fishes[change_fish][0], self.fishes[fish_number][0]
            self.fishes[fish_number][1], self.fishes[change_fish][1] = self.fishes[change_fish][1], self.fishes[fish_number][1]

            # change board
            self.board[fish_r][fish_c], self.board[fish_nr][fish_nc] = self.board[fish_nr][fish_nc], self.board[fish_r][fish_c]

            print('moved ',fish_number)
            self.misc_pprint()
            

        elif shark:
            # move shark to destination
            if destination[0] == -1 and destination[1] == -1:
                return None
            
            self.board[shark_r][shark_c] = [0,0]

            shark_r = self.shark[0]
            shark_c = self.shark[1]
            shark_dir = self.board[shark_r][shark_c][1]

            self.shark[0] = destination[0]
            self.shark[1] = destination[1]
            
            self.board[shark[0]][shark[1]] = -1
        else: 
            return None
    
    def move_fishes(self):
        for i in range(1,17):
            self.move(fish_number=i)

    def move_shark(self, destination):
        self.move(shark=True, destination=destination)

    def shark_in(self):
        if self.board[0][0][0] == 0:
            return False
        else:
            score += self.board[0][0][0]
            self.board[0][0][0] = -1
            self.shark = [0,0]
            return True

    def shark_go_home(self):
        shark_r = self.shark[0]
        shark_c = self.shark[1]

        self.board[shark_r][shark_c] = 0
        self.shark = None

        return True

    def misc_pprint(self):
        for i in range(4):
            print_arr = []
            for j in range(4):
                print_arr.append([*self.board[i][j]])
            
            for j in range(4):
                # print(print_arr)
                dir_tmp = print_arr[j][1]

                print_arr[j][1] = print_strings[dir_tmp]
            
            print(*print_arr)
    

board = [[None for __ in range(4)] for _ in range(4)]
fishes = [[] for __ in range(17)]

for r in range(4):
    row = [*map(int, input().split())]

    for c in range(4):
        # each block
        fish_number = row[c*2]
        fish_dir = row[c*2+1]

        board[r][c] = [fish_number, fish_dir]
        fishes[fish_number] = [r, c, fish_dir]

root_board = Board(board, fishes)

from pprint import pprint
pprint(root_board.board)
pprint(root_board.fishes)
print(root_board.direction)

root_board.move_fishes()
pprint(root_board.board)


