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
    fdLogs.close()
    
    logsDia = dict(sorted(logsDia.items(), key=lambda x:x[0]))
    
    fdOut = open("resposta_data.txt", "w")
    for dia in logsDia.keys():
        fdOut.write (f"dia {logsDia[dia]}\n")
    fdOut.close()
    
    plt.title ("Logs apache por dia")
    plt.ylabel ("# de acessos no dia")
    plt.bar (logsDia.keys(), logsDia.values())
    plt.show()
except FileNotFoundError as e:
    print (f"O arquivo {nomeArqLog} não está acessível.")
    exit()
