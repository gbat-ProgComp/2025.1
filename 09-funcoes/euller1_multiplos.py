def multiplos3_5ate(limite):
    soma = 0
    for k in range(limite):
        if (k % 3 == 0) and (k % 5 == 0):
            soma += k
    print (soma)
