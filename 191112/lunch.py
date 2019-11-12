"""
완전탐색

time = global time

각 경우에 대하여 choice 결정

choice = [ n번째 사람이 선택한 계단의 종류 ]
arr = [ n번째 사람이 계단까지 가는 시간 ]
stair = [ 0, 0 ] # 계단

time += 1 하면서 진행

사용중인 계단에 대해서 stair[계단] -= 1

각 사람에 대해서,
    도착: 시간 == arr[해당사람]일 경우
    
    계단이 사용중이면 arr[해당사람] + 1

    계단이 사용중이 아니면 arr[해당사람] = 0, 계단 = 계단의 길이



    # make choice binary

    for i in range(2 ** N):
        a = ''
        for j in range(N):
            if i & (1 << j):
                # choice 1
                a += '1'
            else:
                # choice 0
                a += '0'
"""

def solve(it, choice, distance):
    # choice: 0 or 1
    # distance: [ distance ]
    distance_b = [*distance]
    global STAIR_INFO

    N = len(choice)
    time = 0
    stair = [[0,0,0], [0,0,0]]

    while True:
        # if it == 39:
        # print('t', time, 'd', distance, 'st', stair)
        time += 1
        for m in range(3):
            for n in range(2):
                if stair[n][m]: stair[n][m] -= 1
        
        if not any(distance) and not any(stair[0]) and not any(stair[1]):
            break
        
        for i in range(N):
            if time == distance[i]:
                if all(stair[choice[i]]):
                    distance[i] += 1
                else:
                    for m in range(3):
                        if not stair[choice[i]][m]:
                            stair[choice[i]][m] = STAIR_INFO[choice[i]]
                            distance[i] = 0
                            break
    # if time == 19: print(it, choice, distance_b)
    # print()
    return time + 1


for T in range(int(input())):    
    STAIR_INFO = []

    N = int(input())
    person, stairList = [], []
    


    for m in range(N):
        line = [*map(int,input().split())]
        for n in range(N):
            if line[n] == 1: person.append((m,n))
            elif line[n] > 1:
                stairList.append((m,n))
                STAIR_INFO.append(line[n])

    M = len(person)
    distanceList = [(abs(x-stairList[0][0])+abs(y-stairList[0][1]), abs(x-stairList[1][0])+abs(y-stairList[1][1])) for x,y in person]
    
    # print(distanceList)
    min_res = 100000

    for i in range(2 ** M):
        case = []
        for j in range(M):
            if i & (1 << j):
                case.append(1)
            else:
                case.append(0)
        # print(case)
        choice = [c for c in case]
        distance = [distanceList[k][choice[k]] for k in range(M)]

        res = solve(i, choice, distance)

        if res < min_res: min_res = res

    print(min_res)


