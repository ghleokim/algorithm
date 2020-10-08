def tri_flip_to_dec(tri:str) -> int:
    res = 0
    i = 0
    
    for t in tri:
        res += int(t) * (3 ** i)
        i += 1

    return res
    
def dec_to_tri(dec:int) -> str:
    res = ""
    while dec >= 3:
        res = str(dec % 3) + res
        dec = dec // 3

    return str(dec) + res

def solution(n):
    return tri_flip_to_dec(dec_to_tri(n))


print(dec_to_tri(3)) # 1
print(dec_to_tri(11)) # 102
print(dec_to_tri(45)) # 1200
print(dec_to_tri(125)) # 11122


print(tri_flip_to_dec('1200')) # 7
print(tri_flip_to_dec('11122')) # 229

