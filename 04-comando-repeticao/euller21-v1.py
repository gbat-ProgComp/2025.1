for n in range (2, 100000):
    somaDivn = 0
    for i in range (1, n//2 + 1):
        if n % i == 0:
            somaDivn += i
       
    if somaDivn > n:     
        n2 = somaDivn
        somaDivn2 = 0
        for i in range (1, n2 // 2 + 1):
            if n2 % i == 0:
                somaDivn2 += i
        
        if n != somaDivn and somaDivn2 == n:
            print (n, somaDivn)