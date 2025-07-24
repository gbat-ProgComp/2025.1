import matplotlib.pyplot as plt

nomeArqLog = "apache.logs"
try:
    fdLogs = open (nomeArqLog, "r")
    logsStatus = {}
    for log in fdLogs:
        status = log.split()[8]
        logsStatus[status] = logsStatus.get(status, 0) + 1
    fdLogs.close()

    plt.bar (logsStatus.keys(), logsStatus.values(), color="green")
    plt.show()
except FileNotFoundError as e:
    print (f"O arquivo {nomeArqLog} não está acessível.")
    exit()
