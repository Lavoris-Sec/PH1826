userLogs = ['Admin123', 'superUSER', 'GOODstudent']
userBYears = [2000, 2010, 2005]


def listMaker1(login_list):
    new_list = []
    for n in login_list:
        new_list.append(n.lower())
    return new_list


def listMaker2(years_list):
    new_list = []
    for n in years_list:
        new_list.append(2026 - n)
    return new_list


newList2 = listMaker2(userBYears)
newList1 = listMaker1(userLogs)

newList3 = [log.lower() for log in userLogs]
newList4 = [2026 - year for year in userBYears]

print(newList1)
print(newList2)

print("------")

print(newList3)
print(newList4)

