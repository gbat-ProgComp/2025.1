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

medias = [(notas[0]*2 + notas[1]*3)/5  for notas in lstNotas]
mediaAlunos = [[lstNomes[pos], medias[pos]] for pos in range(len(medias))]

for mediaAluno in filter (lambda x: x[1] >= 60, mediaAlunos):
    print (f"{mediaAluno[0]:<20s} foi aprovado com {mediaAluno[1]:_>6.2f}")