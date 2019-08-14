# practice02_itoa

def my_itoa():
    pass

i = 1234
neg = False
s = ''
if i < 0:
    neg = True
    i *= -1

while i:
    s += chr(i % 10 + 48)
    i //= 10

if neg:
    s += '-'
s = s[::-1]
print(s, type(s))