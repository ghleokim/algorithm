# import sys
# sys.stdin = open('input/input4839.txt', 'r')

def binarySearch(p, target):
    cnt, start, end = 0, 1, p
    while True:
        cnt += 1
        c = (start + end) // 2
        if c == target:
            return cnt
        elif c < target:
            start = c
        else:
            end = c
    # return cnt


for T in range(int(input())):
    p, a, b = map(int, input().split())

    ca = binarySearch(p, a)
    cb = binarySearch(p, b)

    if ca == cb:
        winner = 0
    elif ca > cb:
        winner = 'B'
    else:
        winner = 'A'

    print('#{0} {1}'.format(T+1, winner))