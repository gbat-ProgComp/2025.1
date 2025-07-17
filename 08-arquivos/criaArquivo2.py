fd = open ("dados4.txt", "w")
dados  = "Este conteúdo foi criado por um \n"
fd.write(dados)
fd.write("programa em Python.\n")
fd.write("Mais uma linha escrita.")
fd.close()