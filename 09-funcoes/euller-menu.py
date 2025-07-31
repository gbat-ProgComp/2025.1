def d(n):
    soma = 0
    for k in range(1, n):
        if n % k == 0:
            soma += k
    return soma

def amigos_ate(limite):
    for n in range(limite):
        divN  = d(n)
        if (n < divN) and (d(divN) == n):
            print (f"amigos: {n} {divN}")

def multiplos3_5ate(limite):
    soma = 0
    for k in range(limite):
        if (k % 3 == 0) and (k % 5 == 0):
            soma += k
    print (soma)

def menu():   
    print (" 1 - Multiplos de 3 e 5")         
    print ("21 - Amigos")
    return int (input("Selecione sua opcao: "))

while True:
    opcao = menu()
    if opcao == 1:
        multiplos3_5ate(1000)
    elif opcao == 21:
        amigos_ate(10000)
    else:
        print ("Opcao invalida.")