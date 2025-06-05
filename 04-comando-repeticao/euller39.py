# Encontre valores para a, b e c, de modo que:
#      a + b + c = p
#      a**2 + b**2 = c**2

maiorComb = 0
maiorP = 0
for p in range (1, 1000):
    combAt = 0
    for a in range (1, p+1):
        for b in range (a, p+1-a):
            c = p - (a + b)
            if c > 0: 
                a2 = a*a
                b2 = b*b
                c2 = c*c
                if (a2 + b2) == c2:
                    print ("para ", p, "=", a, b, c)
                    combAt += 1
                elif (a2 + b2) > c2:
                    break
    if combAt > maiorComb:
        maiorComb = combAt
        maiorP = p
print ("A maior combinacao é para", maiorP, "com", maiorComb)