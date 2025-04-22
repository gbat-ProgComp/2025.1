print ("Calculadora das Raizes de uma Equação de Segundo Grau")

a = int(input("Informe o valor de a = "))
b = int(input("Informe o valor de b = "))
c = int(input("Informe o valor de c = "))

delta = b**2-4*a*c
print("Valor de Delta Δ = ", delta)

x1 = (-b + delta ** (1/2)) / (2 * a)


x2 = (-b - delta ** (1/2)) / (2 * a)
print ("as raízes da esquação de 2 Grau são", x1, x2)

