def check_num(num):
    if len(num) != len(str(int(num))):
        return False
    return True

def calculate(a, b):
    if all([check_num(a), check_num(b)]):
        return str(int(a)+int(b))
    else:
        return False


def solve(num, min_result, min_count, count):
    if len(num) == 1:
        if min_count > count:
            return num, count
        else:
            return min_result, min_count

    for i in range(len(num)-1):
        a = num[:i+1]
        b = num[i+1:]

        res = calculate(a,b)
        if res == False: continue

        mr, mc = solve(res, min_result, min_count, count+1)

        if min_count > mc:
            min_result = mr
            min_count = mc

    return min_result, min_count


def solution(n):

    res = solve(str(n), 10, len(str(n))+1, 0)

    return [res[1], int(res[0])]


print(solution(73425))
print(solution(10007))
print(solution(9))