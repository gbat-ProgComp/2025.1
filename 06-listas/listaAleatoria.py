import random

n = int(input ("Digite o número n: "))
lista = []
for i in range(100):
    lista.append(random.randint(-n, n))
   
for num in lista:
    if num % 2 == 0 and num > 0:
        print (num) 

filtro = filter(lambda x: (x%2 == 0) and (x >= 0), lista)

for num in filtro:
    print (num, end=",")
print()
