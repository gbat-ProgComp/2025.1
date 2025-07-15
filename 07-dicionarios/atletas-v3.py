import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    dados = json.loads(dados)
    atletas = dados["atletas"]
    posicoes = dados["posicoes"]
    clubes = dados["clubes"]
    
    clube_id = 0
    nome_clube = input ("Qual o nome do clube para listar atletas? ").upper()
    for clube in clubes.values():
        if nome_clube == clube["nome_fantasia"].upper():
            clube_id = clube["id"]
            print (f"Identificado {nome_clube} -> {clube_id}")
            break
        
    if clube_id != 0:
        equipe=[]
        for atleta in atletas:
            if atleta["clube_id"] == clube_id: 
                nome_posicao = posicoes[str(atleta["posicao_id"])]["nome"]
                equipe.append( [ atleta["nome"],
                                atleta["apelido"],      
                                nome_posicao,
                                atleta["preco_num"]
                                ]
                            )
        
        equipe.sort (key=lambda x: x[3], reverse=True)
        for atleta in equipe:
            print (f"{atleta[2]:10s} {atleta[1]:20s} {atleta[3]:5.2f}")
    else:
        print ("Clube não encontrado!")    
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")
