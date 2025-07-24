import sys

nomeArqLog = "apache.logs"
try:
    fdLogs = open (nomeArqLog, "r")
    logsHora = {}
    for log in fdLogs:
        inicioTempo = log.find('[')
        FimTempo    = log.find(']')
        tempo = log[inicioTempo+1:FimTempo][:14]
        if tempo in logsHora.keys():
            logsHora[tempo] += 1
        else:    
            logsHora[tempo]  = 1
    fdLogs.close()
    maisOcorr = max (logsHora.items(), key=lambda item: item[1])
    print (f"A data com mais acessos é {maisOcorr[0]} com {maisOcorr[1]}.")

except FileNotFoundError as e:
    print (f"O arquivo {nomeArqLog} não está acessível.")
    exit()
