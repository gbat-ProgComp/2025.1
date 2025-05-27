print ("saiba sua reforma da previdencia")
c = int (input ("Digite o valor da capital inicial: "))
d = int (input ("Deposito mensal: "))
i = int (input ("Taxa mensal: "))
n = int (input ("Quantos meses deseja depositar? "))

saldo = c * (1 + i/100)**n + d*((1 + i/100)**n - (1 + i/100))/(i/100)
print ("seu saldo é:", round(saldo,2))