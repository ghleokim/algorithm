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

from functools import cmp_to_key

def compare(a,b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))

    return 1 if ab >= ba else -1

def solution(numbers):
    res = ""

    rule = [i for i in range(1001)]
    rule.sort(key=cmp_to_key(compare), reverse=True)

    count = [0 for i in range(1001)]
    for n in numbers:
        count[n] += 1
    
    for r in rule:
        res += str(r) * count[r]
    
    if res == "" or res.count(0) == len(res):
        res = "0"
    
    return res

    