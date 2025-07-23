
with open ("apache.logs") as fdLogs, open ("ips.txt", "w") as fdIps:
    ips = set()
    for log in fdLogs:
        ip = log.split()[0]
        if not ip in ips:
            fdIps.write(ip+"\n")
            ips.add(ip)