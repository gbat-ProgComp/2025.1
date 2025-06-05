x = 1
while x <= 100:
    n = x
    tam = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        tam += 1
    print ("a cadeia do ", x, "tem ", tam, "elementos")
    x = x + 1
print ("FIM")