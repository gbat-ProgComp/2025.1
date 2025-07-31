def d(n):
    soma = 0
    for k in range(1, n):
        if n % k == 0:
            soma += k
    return soma

def amigos_ate(limite):
    for n in range(limite):
        divN  = d(n)
        if (n < divN) and (d(divN) == n):
            print (f"amigos: {n} {divN}")
            