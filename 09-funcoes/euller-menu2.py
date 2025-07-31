import euller1_multiplos
import euller21_amigos

def menu():   
    print (" 1 - Multiplos de 3 e 5")         
    print ("21 - Amigos")
    return int (input("Selecione sua opcao: "))

while True:
    opcao = menu()
    if opcao == 1:
        euller1_multiplos.multiplos3_5ate(1000)
    elif opcao == 21:
        euller21_amigos.amigos_ate(10000)
    else:
        print ("Opcao invalida.")