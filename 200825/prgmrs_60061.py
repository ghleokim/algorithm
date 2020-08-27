class Board:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n+1)] for __ in range(n+1)]
    
    def __str__(self):
        i = self.n
        for b in self.board[::-1]:
            print(i, b)
            i -= 1
        return ''
    
    def validate(self, operation):
        is_valid = False

        x, y, a, b = operation
        # 기둥
        if a == 0:
            # 바닥에 있거나
            if y == 0:
                is_valid = True
            # 바로 아래에 기둥이 있거나
            elif self.board[x][y-1] == 2 or self.board[x][y-1] == 3:
                is_valid = True
            # 보의 한쪽 끝 위에 있거나
            elif self.board[x][y] == 1 or self.board[max(0, x-1)][y] == 1 or self.board[max(0, x-1)][y] == 3:
                is_valid = True
        # 보
        else:
            if self.board[x][max(0,y-1)] >= 2 or self.board[x+1][max(0,y-1)] >= 2:
                is_valid = True
            elif self.board[max(0,x-1)][y] in (1,3) and self.board[min(self.n,x+1)][y] in (1,3):
                is_valid = True

        return is_valid

    def build(self, operation):
        if not self.validate(operation):
            return False
        else:
            x, y, a, b = operation
            if a == 0:
                self.board[x][y] += 2
            else:
                self.board[x][y] += 1

            return True
    
    def validate_destroy(self, operation):
        # is valid : 삭제 가능한 조건
        is_valid = True

        x, y, a, b = operation
        if a == 0:
            if self.board[x][y+1] >= 2:
                is_valid = False

            # 바로위에 보
            elif x < self.n and self.board[x][y+1] == 1:
                if self.board[x+1][y] >= 2:
                    is_valid = False
                elif x < self.n-1 and self.board[x+2][y+1] in (1, 3):
                    is_valid = False
            # 상단 좌측 보
            elif x > 0 and self.board[x-1][y+1] == 1:
                if self.board[x-1][y] >= 2:
                    is_valid = False
                elif x > 1 and self.board[x-2][y+1] in (1, 3):
                    is_valid = False

        else:
            # 같은 장소에 기둥이 있고 좌측에 보 없을 때
            if x > 0 and self.board[x][y] >= 2 and self.board[x-1][y] in (0,2):
                is_valid = False
            # 우측에 기둥이 있고 우측에 보 없을 때
            elif x < self.n and self.board[x+1][y] == 2:
                is_valid = False
            # x > 1, 같은 장소에 기둥이 없고 좌측에 보 있고 그 좌측에 보 없거나 좌측 아래에 기둥이 없을 때
            elif x > 1 and self.board[x][y] <= 2 and self.board[x-1][y] in (1,3) and (self.board[x-2][y] in (0,2) or self.board[x-1][y-1] <= 2):
                is_valid = False
            # x < self.n, 우측에 기둥이 없고 우측에 보 있고 그 우측에 보 없거나 우측 아래에 기둥이 없을 때
            elif x < self.n-1 and self.board[x+1][y] == 1 and (self.board[x+2][y] in (0,2) or self.board[x+1][y-1] <= 2):
                is_valid = False

        return is_valid

    def destroy(self, operation):
        x, y, a, b = operation
        if not self.validate_destroy(operation):
            return False

        if a == 0:
            self.board[x][y] -= 2
        else:
            self.board[x][y] -= 1        
            
        return True

    def operate(self, operation):
        if operation[3] == 1:
            return self.build(operation)
        else:
            return self.destroy(operation)
    
    def get_answer(self):
        answer = []
        for i in range(self.n+1):
            for j in range(self.n+1):
                b = self.board[i][j]
                if b == 1:
                    answer.append([i,j,1])
                elif b == 2:
                    answer.append([i,j,0])
                elif b == 3:
                    answer.append([i,j,0])
                    answer.append([i,j,1])
        return answer

def solution(n, build_frame):
    board = Board(n)
    
    for operation in build_frame:
        res = board.operate(operation)
    print(board)
    answer = board.get_answer()
    print(answer)
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 =[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
build_frame3 =[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1],[2,1,1,0]]

solution(n, build_frame3)