salarioBruto = float(input("Informe o salario bruto: "))

if salarioBruto <= 2428.80:
    imposto = 0
else:
    if 2428.81 <= salarioBruto <= 2826.65:
        imposto = salarioBruto * (7.5/100) - 182.16
    else:
        if 2826.66 <= salarioBruto <= 3751.05:
            imposto = salarioBruto * (15/100) - 394.16
        else:
            if 3751.06 <= salarioBruto <= 4664.86:
                imposto = salarioBruto * (22.5/100) - 675.49
            else:
                imposto = salarioBruto * (27.5/100) - 908.73
                
salarioLiquido = salarioBruto - imposto
print ("O imposto é:", imposto)
print ("O salario líquido é:", salarioLiquido)