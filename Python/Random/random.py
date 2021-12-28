hd = 0
a = "1"
b = "100"
if len(a) > len(b):
    b = b[::-1]
    for i in range(len(a) - len(b)):
        b += '0'
    b = b[::-1]
else:
    a = a[::-1]
    for i in range(len(b) - len(a)):
        a += '0'
    a = a[::-1]
for i in range(len(a)):
    if a[i] != b[i]:
        hd += 1
print(hd)