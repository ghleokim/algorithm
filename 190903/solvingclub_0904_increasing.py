# 0 1 2 3 중 두 개 조합
    
for T in range(int(input())):
    def inc1(num):
        n = str(num)
        for i in range(len(n)-1):
            if n[i] > n[i+1]: return False
        return True
        
    def inc2(num):
        if sorted(str(num)) != [*str(num)]: return False
        return True

    # print(inc1(123), inc2(123))
    # print(inc1(213), inc2(213))

    def backtrack(res=[]):
        global vis, mx
        for i in range(len(nums)):
            if not vis[i]:
                vis[i] = 1
                res.append(i)
                if len(res)==1:
                    backtrack([*res])
                if len(res)==2:
                    # do something
                    tmp = nums[res[0]] * nums[res[1]]
                    if mx < tmp and inc1(tmp): mx = tmp
                vis[i] = 0
                res.pop()
        
    input()
    # tmp = [*map(int,input().split())]
    nums = [*map(int,input().split())]

    vis = [0 for i in range(len(nums))]
    mx = -1
    backtrack()
    print('#',end='')
    print(T+1,mx)

"""
1
4
2 4 7 10
"""