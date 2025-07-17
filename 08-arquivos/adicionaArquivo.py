fd = open ("dados3.txt", "a")
dados  = "Estamos adicionando esse conteúdo ao arquivo original.\n"
fd.write(dados)
fd.close()