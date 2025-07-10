num = input ("Digite um número: ")
try:
    numInteiro = int(num)
except:
    print ("Voce digitou um numero errado, supondo 0.")
    numInteiro = 0
dobro = 2 * numInteiro
print ("O dobro de", numInteiro, "é", dobro)