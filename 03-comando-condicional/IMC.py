peso   = float(input("Informe seu peso (em Kg): "))
altura = float(input("Informe sua altura (em cm): "))
imc = round(peso / (altura/100) ** 2, 1)

if imc < 18.5:
    classificacao = "Magreza"
    obesidade = 0
if 18.5 <= imc <= 24.9:
    classificacao = "Normal"
    obesidade = 0
if 25.0 <= imc <= 29.9:
    classificacao = "Sobrepeso"
    obesidade = 1
if 30.0 <= imc <= 39.9:
    classificacao = "Obesidade"
    obesidade = 2
if imc >= 40:
    classificacao = "Obesidade grave"
    obesidade = 3
                
print ("IMC:", imc)
print ("Classificao:", classificacao)
print ("Nivel de obsidade:", obesidade)