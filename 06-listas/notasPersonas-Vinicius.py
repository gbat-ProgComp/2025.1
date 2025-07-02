##### primeira parte que Galileu fez em sala #####

import random

VERMELHO = '\033[31m'
VERDE = '\033[32m'
PADRAO = '\033[0m'

Alunos = ['Scooby-Doo'         , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]
Lista_Notas =[]
for a in range(len(Alunos)):
    Lista_Notas += [[random.randint(0,100),random.randint(0,100),random.randint(0,100)]]

##### primeira parte que Galileu fez em sala #####

Medias = []
Aluno_Media = []
Alunos_Medias = []
Aluno_Aprovado = []
Alunos_Aprovados = []
Aluno_Reprovado = []
Alunos_Reprovados = []
for cont in range(len(Lista_Notas)): 
    #### entra dentro da lista: Lista_Notas ####
#####################################################################################
    notas = Lista_Notas[cont]
    #### pega os dois primeiros elementos de notas e faz a média ####
    Medias.append(((notas[0]*2) + (notas[1]*3))/5)
    #### pega os dois primeiros elementos de notas e faz a média ####
#####################################################################################
    ### cria uma lista de apenas alunos com suas respectivas médias ### 
    Aluno_Media = [Alunos[cont], Medias[cont]]
    Alunos_Medias += [Aluno_Media]
    ### cria uma lista de apenas alunos com suas respectivas médias ###

#####################################################################################
    ### cria uma lista de alunos passados por média e suas respectivas médias ###
    if Aluno_Media[1] >= 60:
        Aluno_Aprovado = []
        Aluno_Aprovado += [Aluno_Media[0]]
        Aluno_Aprovado += [Aluno_Media[1]]
        Alunos_Aprovados += [Aluno_Aprovado]
    ### cria uma lista de alunos passados por média e suas respectivas médias ###
#####################################################################################    
    ### cria uma lista de alunos que ficaram de recuperação ou reprovados e suas respectivas médias ###
    else:
        Aluno_Reprovado = []
        Aluno_Reprovado += [Aluno_Media[0]]
        Aluno_Reprovado += [Aluno_Media[1]]
        Alunos_Reprovados += [Aluno_Reprovado]
    ### cria uma lista de alunos que ficaram de recuperação ou reprovados e suas respectivas médias ###
    
    ### exibe todos os alunos e suas respectivas médias ###
    if Aluno_Media[1] >= 60:
        print(f'a nota do {VERDE}{Aluno_Aprovado[0]}{PADRAO} foi:{VERDE}{Aluno_Aprovado[1]}{PADRAO}')
    else:
        print(f'a nota do {VERMELHO}{Aluno_Reprovado[0]}{PADRAO} foi:{VERMELHO}{Aluno_Reprovado[1]}{PADRAO}')
    ### exibe todos os alunos e suas respectivas médias ###

########################################## exibe a situação do aluno ##########################################
for cont in range(len(Alunos_Aprovados)):
    Aluno_Aprovado = Alunos_Aprovados[cont]
    print(f'parabéns {VERDE}{Aluno_Aprovado[0]}{PADRAO} você foi {VERDE}aprovado{PADRAO}!!!')
    

for cont in range(len(Alunos_Reprovados)):
    Aluno_Reprovado = Alunos_Reprovados[cont]
    print(f'sinto muito {VERMELHO}{Aluno_Reprovado[0]}{PADRAO} você ficou de {VERMELHO}recuperação{PADRAO}!!!')
########################################## exibe a situação do aluno ##########################################