while True:
    try:
        num = int(input ("Digite o numerador: "))
        den = int(input ("Digite o numerador: "))
        print (num/den)
        break
    except ValueError as e1:
        print ("Erro de digitacao!")
    except ZeroDivisionError as e2:
        print ("Erro de divisão por zero!!")
    except:
        print ("Erro por outro motivacao!")
        