x = 1
maiorTam = 0 
geradorMaior = 0
while x <= 1000000:
    n = x
    tam = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        tam += 1
    #print ("a cadeia do ", x, "tem ", tam, "elementos")
    if tam > maiorTam:
        maiorTam = tam
        geradorMaior = x
    x = x + 1
print ("FIM - o maior tamanho  é:", maiorTam, "na sequencia do ", geradorMaior)