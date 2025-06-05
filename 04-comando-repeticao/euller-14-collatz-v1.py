x = 1
while x <= 10:
    n = x
    print ("seq", n, end="")
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print ("->", n, end="")
    print ()
    x = x + 1
print ("FIM")