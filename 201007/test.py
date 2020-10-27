import functools
a = [3,2,2,2,3]

# 오름차순 정렬
def compare(x,y):
    return x - y

b = sorted(a, key=enumerate(a))
print(b) # [2,2,3]