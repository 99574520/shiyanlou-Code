a = 0
while a < 100:
    a = a + 1
    if a == 7:
        continue
    b = a % 7
    c = a % 10
    d = a //10
    if b == a or c == 7 or d == 7:
        continue
    print(a)
