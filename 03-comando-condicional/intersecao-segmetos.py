# Programa para determinar interseção der segmentos de reta

# Entrada dos valores
ai = int (input("Início segmento 1: "))
af = int (input("Final  segmento 1: "))
bi = int (input("Início segmento 2: "))
bf = int (input("Final  segmento 2: "))

# Verifica a interseção
if bi > af:
    print ("Sem interseção!") 
else:
    if ai > bf:
        print ("Sem interseção!") 
    else:
        print ("Com interseção!") 
