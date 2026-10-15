userLogs = ['123user45', 'USERstudent', '56use3', 'user-23', 'adminUs']
lower_logs = []

for log in userLogs:
    lower_logs.append(log.lower())

print(lower_logs)


lower_logs_2 = [log.lower() for log in userLogs]

print(lower_logs_2)


lower_logs_3 = list(map(str.lower, userLogs))

print(lower_logs_3)