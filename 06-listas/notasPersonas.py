import random

lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

lstNotas = []
for n in range(len(lstNomes)):
    lstNotas.append([random.randint(0,100), 
                     random.randint(0,100), 
                     random.randint(0,100)])

for pos in range(len(lstNomes)):
    print (lstNomes[pos], lstNotas[pos])
