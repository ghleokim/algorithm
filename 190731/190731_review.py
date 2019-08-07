import sys
sys.stdin = open('input.txt', 'r')

for en in range(10):
    length = input()
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, len(building)-2):
        compare = [0] * 4
        if building[i] > building[i+2] and building[i] > building[i-2]:
            if building[i] > building[i+1] and building[i] > building[i-1]:
                compare[0] = building[i] - building[i-2]
                compare[1] = building[i] - building[i-1]
                compare[2] = building[i] - building[i+1]
                compare[3] = building[i] - building[i+2]

                for c in range(4, -1, -1):
                    for d in range(c - 1):
                        if compare[d] > compare[d + 1]:
                            compare[d], compare[d + 1] = compare[d + 1], compare[d]

                result += compare[0]

    print('#{0} {1}'.format(en + 1, result))
