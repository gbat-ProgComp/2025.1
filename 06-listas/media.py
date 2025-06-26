soma = 0
qtdeNum = 0

num = int (input("Digite um numero: "))
while num > 0:
    soma += num
    qtdeNum += 1
    num = int (input("Digite um numero: "))

if qtdeNum > 0:
    media = soma / qtdeNum