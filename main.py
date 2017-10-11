def kol(n):
    k = 0
    while n > 0:
        n = n // 10
        k += 1
    return k

for i in range(1000):
    if kol(i) == kol(3*i) and kol(i) == kol(4*i):
        print(i, 3*i, 4*i)