import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    dados = json.loads(dados)
    atletas = dados["atletas"]
    posicoes = dados["posicoes"]
    
    botafogo=[]
    for atleta in atletas:
        if atleta["clube_id"] == 263: # Botafogo/RJ
            nome_posicao = posicoes[str(atleta["posicao_id"])]["nome"]
            botafogo.append( [ atleta["nome"],
                               atleta["apelido"],      
                               nome_posicao,
                               atleta["preco_num"]
                             ]
                            )
    
    botafogo.sort (key=lambda x: x[3], reverse=True)
    for atleta in botafogo:
        print (f"{atleta[2]:10s} {atleta[1]:20s} {atleta[3]:5.2f}")
    
    
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")
