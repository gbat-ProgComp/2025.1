print ("Esse programa mostra cédulas de um troco")
conta = int(input("Valor da conta: "))
pago  = int(input("Valor pago: "))
troco = pago - conta
print ("O troco é: ", troco)

notas200 = troco // 200
if notas200 > 0:
    print ("Notas de 200:", notas200)
    troco = troco % 200

notas100 = troco // 100
if notas100 > 0:
    print ("Notas de 100:", notas100)
    troco = troco % 100

notas50 = troco // 50
if notas50 > 0:
    print ("Notas de 50:", notas50)
    troco = troco % 50

notas20 = troco // 20
if notas20 > 0:
    print ("Notas de 20:", notas20)
    troco = troco % 20

notas10 = troco // 10
if notas10 > 0:
    print ("Notas de 10:", notas10)
    troco = troco % 10

notas5 = troco // 5
if notas5 > 0:
    print ("Notas de 5:", notas5)
    troco = troco % 5

notas2 = troco // 2
if notas2 > 0:
    print ("Notas de 2:", notas2)
    troco = troco % 2

if troco > 0:
    print ("Moedas de 1:", troco)