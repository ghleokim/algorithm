# {1,2,3,4,5,6,7,8,9,10}의 powerset중 원소의 합이 10인 부분집합

def backtrack(k, s):
    global cnt
    cnt += 1
    if k == N:
        if s == 10:
            for i in range(1,11):
                if a[i]:
                    print(i, end=' ')
            print()
    else:
        k += 1
        if s + k <= 10:
            a[k] = 1; backtrack(k, s+k)
        # a[k] = 1; backtrack(k, s+k)
        a[k] = 0; backtrack(k, s)
N = 10
a = [0] * (N+1)


cnt = 0
backtrack(0,0)
print(cnt)

# ---------------------------------------- #

