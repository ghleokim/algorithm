t = int(input())

for _ in range(t):
    n = int(input())
    password = [*map(int, input().split())]

    while len(set(password)) != 1:
        for i in range(n-1):
            if password[i] == password[i+1]:
                continue
            else:
                addition = password[i]
                password = password[:i] + password[i+1:]
                password[i] += addition
                break
        
        n -= 1
    
    print(len(password))
