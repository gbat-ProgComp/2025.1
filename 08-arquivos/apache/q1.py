import sys

nomeArqLog = "apache.logs"
try:
    fdLogs = open (nomeArqLog, "r")
    logsMinuto = {}
    for log in fdLogs:
        inicioTempo = log.find('[')
        FimTempo    = log.find(']')
        tempo = log[inicioTempo+1:FimTempo][:17]
        if tempo in logsMinuto.keys():
            logsMinuto[tempo] += 1
        else:    
            logsMinuto[tempo]  = 1
    fdLogs.close()
    for minuto in logsMinuto:
        print (f"{minuto} => {logsMinuto[minuto]}")
except FileNotFoundError as e:
    print ("O arquivo {nomeArqLog} não está acessível.")
    exit()
