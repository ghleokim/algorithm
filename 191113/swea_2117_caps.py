"""

집 갯수 최대 20*20 = 400개

방범 시작 위치 최대 400개

N*N을 커버하기 위한 K의 최댓값 : N+1

최대 계산량 400 * 400 * 10 = 1600000


position | house
px, py,    hx, hy
top, bottom, left, right = hy + K-1, hy - (K-1), hx - (K-1), hx + K-1
conditions:
    1) hx >= px, hy >= py, hx + hy <= px + py
    2) hx >= px, hy < py, hy - hx <= py - px
    3) hx < px, hy >= py, hx - hy <= px - py
    4) hx < px, hy < py, hx + hy >= px + py


"""


# def check_houses(pos, K): # input: start position, K
#     global N
#     px, py = pos
#     top, bottom, left, right = py + K-1, py - (K-1), px - (K-1), px + K-1
#     print(pos,top,bottom,left,right)

#     for hx, hy in house:
#         # get boundary block
#         # hx, hy should be in...
#         # max(0, left) < hx < min(N, right)
#         # max(0, bottom) < hy < min(N, top)

#         if max(0, left) <= hx <= min(N, right) and max(0, bottom) <= hy <= min(N, top):
#             # vishouse[hx][hy] = '#'
#             print(hx, hy, px, py, left, py, hx - hy , left - py)
#             # conditions
#             if abs(hx-px)+abs(hy-py) < K: vishouse[hx][hy] = '#'
#             # if all((hx >= px, hy >= py, hx + hy <= py + right)): print('inside'); vishouse[hx][hy] = '#'
#             # elif all((hx >= px, hy < py, hx - hy <= left - py)): print('inside'); vishouse[hx][hy] = '#'
#             # elif all((hx < px, hy >= py, hx - hy >= right - px)): print('inside'); vishouse[hx][hy] = '#'
#             # elif all((hx < px, hy < py, hx + hy >= left + py)): print('inside'); vishouse[hx][hy] = '#'
#             else:
#                 vishouse[hx][hy] = '_'
#         else:
#             print('outside'); vishouse[hx][hy] = '.'



def check_houses(pos, K): # input: start position, K
    global N, M, max_res, max_profit
    count = 0
    profit = - (K**2 + (K-1)**2)
    px, py = pos 

    top, bottom, left, right = py + K-1, py - (K-1), px - (K-1), px + K-1   

    for hx, hy in house:
        # get boundary block
        # hx, hy should be in...
        # max(0, left) < hx < min(N, right)
        # max(0, bottom) < hy < min(N, top)

        if max(0, left) <= hx <= min(N, right) and max(0, bottom) <= hy <= min(N, top):
            # conditions
            if abs(hx-px)+abs(hy-py) < K:
                profit += M
                count += 1


    if profit > 0 and count > max_res:
        max_res = count
    

for T in range(int(input())):
    N, M = map(int,input().split())
    house = []

    i=0
    for _ in range(N):
        j=0
        line = [*map(int,input().split())]
        for p in line:
            if p: house.append((i,j))
            
            j += 1
        i += 1



    max_res = -500000
    max_profit = -500000

    for pos in range(N**2):
        px, py = pos // N, pos % N
        for K in range(N+2):
            check_houses((px,py),K)

    print('#', end='')
    print(T+1, max_res)
    # print(house)
