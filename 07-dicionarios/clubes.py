import requests, json

try:
    clubes = requests.get("https://api.cartola.globo.com/clubes").text
    dClubes = json.loads(clubes)
    for clube in dClubes.values():
        if clube["nome"] == "BOT":
            print (clube["id"], clube["nome_fantasia"])
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")
