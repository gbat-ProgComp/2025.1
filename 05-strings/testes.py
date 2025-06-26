s = "MariaLuiza"

print (s[1:5])  # aria
print (s[0:5])  # Maria
print (s[:5])   # Maria
print (s[0:10])   # MariaLuiza

pos = 3
print (s[pos:pos+2])   # ia
print (s[pos:len(s)])  # iaLuiza
print (s[0:len(s)])    # MariaLuiza

print (s[:len(s):2])    # Mrauz
print (s[::])           # MariaLuiza
print (s[::2])          # Mrauz
print (s[1:5:-1])       # 
print (s[5:1:-1])       # Lair


n = "Giovanna"
print (n[-8:-6])        # Gi
print (n[-8:-4])        # Giov
print (n[-8:-4:2])      # Go
print (n[:4:-1])        # ann
print (n[::-1])         # annavoiG

print (n[2+3*5-10-3.2:4])
x = input ("Digite um numero: ")
y = x[::-1]

if x == y:
    print ("palindromo")