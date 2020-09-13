def get_candi(n):
    candi = []

    for i in range(2**n):
        cur_res = 0
        for j in range(n):
            if i & (1 << j):
                cur_res += 11
            else:
                cur_res += 1
        candi.append(cur_res)
    return list(set(candi))

print(get_candi(3))
print(get_candi(2))
print(get_candi(1))