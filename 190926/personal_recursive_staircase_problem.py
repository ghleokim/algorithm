# recursive staircase problem:
# problem from youtube: https://www.youtube.com/watch?v=5o-kdjv7FD0
# 1) given N: count ways to climb stairs
# climbing stairs with only 1, 2 at a time
# get num_ways(N)
# 2) given N, X: X is {1,3,5} for example
# get num_ways(N,X)

# 1) 

N = 4

def num_ways(N):
    if N == 0 or N == 1:
        return 1
    else:
        return num_ways(N-1) + num_ways(N-2)
        
print(num_ways(N))

def bottom_up(N):
    if N == 0 or N == 1:
        return 1
    nums = [0] * (N+1)
    nums[0], nums[1] = 1, 1
    for i in range(2,N+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[-1]

print(bottom_up(N))

def bottom_up_advanced(N):
    nums = [1, 1]
    for i in range(2, N+1):
        nums[0], nums[1] = nums[1], nums[0] + nums[1]
    return nums[-1]

print(bottom_up_advanced(N))

# 2) X = set of numbers of steps going up the stairs
def num_ways2(N, X):
    nums = [0] * (N+1)
    nums[0] = 1
    for i in range(1, N+1):
        total = 0
        for j in X:
            if N >= j:
                total += nums[i-j]
        nums[i] = total
    return nums[-1]

print(num_ways2(N,[1,2]))

