# 0 상 1 하 2 좌 3 우

N = int(input())

atoms = [0 for _ in range(N)]

for i in range(N):
    atoms[i] = [*map(int, input().split())]

time = [[] for _ in range(4000)]

for i in range(N):
    #상
    if atoms[i][2] == 0:
        for j in range(N):
            if atoms[i][1] < atoms[j][1] and atoms[j][2] == 1:
                dist = atoms[j][1]-atoms[i][1]
                time[dist].append((i, j))
            if abs(atoms[j][0]-atoms[i][0]) == abs(atoms[j][1]-atoms[i][0]) and atoms[i][1] < atoms[j][1]:
                if atoms[j][0] > atoms[i][0] and atoms[j][2] == 2:
                    time[dist].append((i,j))
                elif atoms[j][0] < atoms[i][0] and atoms[j][2] == 3:
                    time[dist].append((i,j))
    #하
    elif atoms[i][2] == 1:
        for j in range(N):
            if atoms[i][1] > atoms[j][1] and atoms[j][2] == 0:
                dist = atoms[i][1]-atoms[j][1]
                time[dist].append((i, j))
            if abs(atoms[j][0]-atoms[i][0]) == abs(atoms[j][1]-atoms[i][0]) and atoms[i][1] > atoms[j][1]:
                if atoms[j][0] > atoms[i][0] and atoms[j][2] == 2:
                    dist = atoms[j][0] - atoms[i][0]
                    time[dist].append((i,j))
                elif atoms[j][0] < atoms[i][0] and atoms[j][2] == 3:
                    dist = atoms[i][0] - atoms[j][0]
                    time[dist].append((i,j))
    #좌
    elif atoms[i][2] == 2:
        pass
        for j in range(N):
            if atoms[i][0] > atoms[j][0] and atoms[j][2] == 3:
                dist = atoms[j][1]-atoms[i][1]
                time[dist].append((i, j))
            if abs(atoms[j][0]-atoms[i][0]) == abs(atoms[j][1]-atoms[i][0]) and atoms[i][1] > atoms[j][1]:
                if atoms[j][0] > atoms[i][0] and atoms[j][2] == 2:
                    time[dist].append((i,j))
                elif atoms[j][0] < atoms[i][0] and atoms[j][2] == 3:
                    time[dist].append((i,j))
    else:
        
        pass

print(time)