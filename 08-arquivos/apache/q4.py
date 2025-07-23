import sys 
import matplotlib.pyplot as plt 

nomeArqLog = "apache.logs"
try:
    fdLogs = open (nomeArqLog, "r")
    logsDia = {}
    for log in fdLogs:
        inicioTempo = log.find('[')
        FimTempo    = log.find(']')
        tempo = log[inicioTempo+1:FimTempo][:11]
        if tempo in logsDia.keys():
            logsDia[tempo] += 1
        else:    
            logsDia[tempo]  = 1
    
    logsDia = dict(sorted(logsDia.items(), key=lambda x:x[0]))
    
    plt.title ("Logs apache por dia")
    plt.ylabel ("# de acessos no dia")
    plt.bar (logsDia.keys(), logsDia.values())
    plt.show()
    fdLogs.close()

        
except FileNotFoundError as e:
    print ("O arquivo {nomeArqLog} não está acessível.")
    exit()
