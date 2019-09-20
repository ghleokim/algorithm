def check(bnum, tnum):
    global result

    n = 0
    b2d = 0
    for b in bnum[::-1]:
        b2d += int(b) * 2 ** n
        n += 1

    n = 0
    t2d = 0
    for t in tnum[::-1]:
        t2d += int(t) * 3 ** n
        n += 1

    print(b2d, t2d)
    if b2d == t2d:
        result = b2d
        return True
    else:
        return False

for T in range(int(input())):
    found = False
    result = 0

    binNum = list(input())
    triNum = list(input())


    for i in range(len(binNum)):
        if binNum[i] == '0':
            binNum[i] = '1'
        else:
            binNum[i] = '0'
        for j in range(len(triNum)):
            if triNum[j] == '0':
                triNum[j] = '1'
                if check(binNum, triNum): found = True; break
                triNum[j] = '2'
                if check(binNum, triNum): found = True; break
                triNum[j] = '0'
            elif triNum[j] == '1':
                triNum[j] = '0'
                if check(binNum, triNum): found = True; break
                triNum[j] = '2'
                if check(binNum, triNum): found = True; break
                triNum[j] = '1'
            else:
                triNum[j] = '0'
                if check(binNum, triNum): found = True; break
                triNum[j] = '1'
                if check(binNum, triNum): found = True; break
                triNum[j] = '2'
        if found: print(binNum, triNum); break

        if binNum[i] == '0':
            binNum[i] = '1'
        else:
            binNum[i] = '0'

    print('#', end='')
    print(T+1, result)