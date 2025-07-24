import sys 
import matplotlib.pyplot as plt 

nomeArqLog = "apache.logs"
try:
    fdLogs = open (nomeArqLog, "r")
    
    # O dicionario logsDia tera a seguinte informação:
    #     { dia1 : { ip1 : #acessos, ip2: #acessos, ip3: #acessos },
    #       dia2 : { ip1 : #acessos, ip2: #acessos, ip3: #acessos },
    #       ...
    #     }
    logsDia = {}
    for log in fdLogs:
        ip = log[:log.find(' ')]
        inicioTempo = log.find('[')
        FimTempo    = log.find(']')
        dia = log[inicioTempo+1:FimTempo][:11]
        
        # Encontra o dicionario com os ips e acessos do dia
        if dia in logsDia.keys():
            ipsDia = logsDia[dia]
        else:    
            ipsDia = {}
        
        # Adiciona um acesso ao dicionario de acessos do dia
        if ip in ipsDia.keys():
            ipsDia[ip] += 1
        else:
            ipsDia[ip]  = 1
            
        # Atualiza o dicionario com ips/acessos do dia 
        logsDia[dia] = ipsDia
    fdLogs.close()
    
    for dia in logsDia:
        print (dia, max(logsDia[dia].items(), key=lambda x:x[1]))
except FileNotFoundError as e:
    print (f"O arquivo {nomeArqLog} não está acessível.")
    exit()
