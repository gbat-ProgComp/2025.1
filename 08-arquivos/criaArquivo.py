fd = open ("dados2.txt", "w")
dados  = "Este conteúdo foi criado por um \n"
dados += "programa em Python\n"
fd.write(dados)
fd.close()