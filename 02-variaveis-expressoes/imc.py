print ("Esse programa calcula o IMC")
peso   = int(input("Digite o seu peso: "))
altura = int(input("Digite a sua altura (em cm): "))
imc   = peso / ((altura / 100) ** 2)
print ("O IMC eh:", imc)

