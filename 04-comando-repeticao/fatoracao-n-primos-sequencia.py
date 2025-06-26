# Encontrar a primeira sequencia de números consecutivos 
# que têm NFATORES distintos
# Assim:
#
#     14 e 15 
#       são 2 números em sequencia 
#       todos tem 2 fatores primos distintos
# 
#     644 645 e 646 
#         são 3 números em sequencia 
#         todos tem 3 fatores primos distintos 
# 
#     134043 134044 134045 134046 
#         são 4 números em sequencia 
#         todos tem 4 fatores primos distintos 

NFATORES = 4

fatSeq = 0
lastNFat = 0
num = 1

while True:
    curN = num
    div  = 2
    # Descobre quantos fatores primos num tem.
    nFat = 0
    while curN > 1:
        if curN % div == 0:
            nFat += 1
            while curN % div == 0:
                curN //= div
        else:
            div += 1

    # Verifica se os ultimos num-1 numeros tem 
    # o mesmo numero de divisores  (NFATORES)
    if (lastNFat == nFat) and (nFat==NFATORES):
        fatSeq += 1
        if fatSeq == NFATORES: 
            for n in range (num-NFATORES+1, num+1):
                print (n, end= " ")
            print ()
            break
    else:
        lastNFat = nFat
        fatSeq = 1
    
    num += 1    

    if num % 10000 == 0:
        print (num)