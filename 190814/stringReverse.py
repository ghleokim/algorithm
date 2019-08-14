# practice01

original = 'original string'

reverse = [0]*len(original)
print(reverse)

# 자신에서 문자열 뒤집기
for n in range(len(original)//2):
    swap = original[n]
    reverse[n] = original[-(n+1)]
    reverse[-(n+1)] = swap
    print(reverse)

if len(original) % 2:
    reverse[len(original)//2] = original[len(original)//2]
    print(reverse)
    
print(''.join(reverse))

