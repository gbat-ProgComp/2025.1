import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    atletas = json.loads(dados)["atletas"]
    
    '''   for atleta in atletas:
        if atleta["clube_id"] == 263: # Botafogo/RJ
            print (f"{atleta['apelido']} -> {atleta['nome']}")
    '''
    botafogo = filter (lambda x: x['clube_id'] == 263, atletas)
    for atleta in botafogo:
        print (f"{atleta['apelido']} -> {atleta['nome']}")
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")
