# Programa para determinar interseção der segmentos de reta

# Entrada dos valores
ai = int (input("Início segmento 1: "))
af = ai + int (input("Tamanho do segmento 1: "))
bi = int (input("Início segmento 2: "))
bf = bi + int (input("Tamanho do segmento 2: "))

# Ordena os pares, se necessario
if af < ai:
    af, ai = ai, af

if bf < bi:
    bf, bi = bi, bf

# Verifica a interseção
if bi > af:
    print ("Sem interseção!") 
else:
    if ai > bf:
        print ("Sem interseção!") 
    else:
        print ("Com interseção!") 
