from random import randint

# Cores para aprovado/reprovado
branco   = '\033[0m'
vermelho = '\033[91m'
verde    = '\033[92m'
azul     = '\033[94m'

# Listas
lstnomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

lstnotas      = []
lstnotasoma   = []
lstmedia      = []
lstaprovados  = []
lstreprovados = []

# Dar 3 notas para cada nome
for nome in range(len(lstnomes)):
    lstnotas.append([randint(0,100),
                     randint(0,100),
                     randint(0,100)])

# Somar estas notas   
for notas in lstnotas:
    lstnotasoma.append(sum(notas))

# Fazer as médias
for soma in lstnotasoma:
    lstmedia.append(round(soma/3))

# Dar o veredito
for pos in range(len(lstnomes)):
    if lstmedia[pos] >= 60: 
        aprovado = f'{verde}aprovado{branco}'
        lstaprovados.append(f'{azul}{lstnomes[pos]}{branco} foi {aprovado} com {lstmedia[pos]}  ')
    else:
        aprovado = f'{vermelho}reprovado{branco}'
        lstreprovados.append(f'{azul}{lstnomes[pos]}{branco} foi {aprovado} com {lstmedia[pos]}  ')

print(f'Lista de {verde}aprovados{branco}:')   
for aprovados in lstaprovados:
    print(aprovados)
print('-'*100)
print(f'Lista de {vermelho}reprovados{branco}:')   
for reprovados in lstreprovados:
    print(reprovados)