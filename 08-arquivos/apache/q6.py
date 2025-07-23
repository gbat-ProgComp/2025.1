
fdLogs = open ("apache.logs", "r")
ips = set()
for log in fdLogs:
    ip = log.split()[0]
    ips.add(ip)
fdLogs.close()

fdIps = open ("ips.txt", "w")
for ip in ips:
    fdIps.write(ip+"\n")
fdIps.close()