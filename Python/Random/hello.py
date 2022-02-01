var = 0
for i in range(20):
    if i % 2 == 0:
        var += 1
        var *= i
    else:
        var -= i
    print(var)
