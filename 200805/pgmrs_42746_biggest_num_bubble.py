"""
999 99_ 9__
998 997 996 ... 990
989 98_ 
988 987 986 ... 980
...
"""
# 9 > 901 > 900 > 8

# 9 99 999 998 997 996 ... 990
# 98 989 987 ...

def compare(a,b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))

    return 1 if ab >= ba else -1


def solution(numbers):
    res = ""

    rule = [_ for _ in range(1001)]
    for i in range(len(rule)):
        for j in range(len(rule)):
            if compare(rule[i], rule[j]) == 1:
                rule[i], rule[j] = rule[j], rule[i]
    
    count = [0 for _ in range(1001)]
    for n in numbers:
        count[n] += 1
    
    for r in rule:
        res += str(r) * count[r]
    
    if res == "" or res.count("0") == len(res):
        res = "0"
    
    return res


solution([1,2,3,4])