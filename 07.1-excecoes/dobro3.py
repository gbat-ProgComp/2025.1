num = input ("Digite um número: ")

while True:
    try:
        numInteiro = int(num)
        break
    except:
        print ("Erro na digitacao!!!")
        
dobro = 2 * numInteiro
print ("O dobro de", numInteiro, "é", dobro)