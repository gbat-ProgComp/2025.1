fd = open ("dados1.txt", "r")
for linha in fd:
    print (linha)
fd.close()