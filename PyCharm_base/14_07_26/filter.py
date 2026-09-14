prices = [100.45, 8.56, 5, 234, 45, 87, 567]

filt_p = list(filter(lambda x: x > 10, prices))

print(filt_p)

#

userLogs = ['123user45', 'USERstudent', '56use3', 'user-23', 'adminUs']


def check_logs(user):
    user_m = user.lower()
    if user_m.find('user') != -1:
        return user


mod_userLogs = list(filter(check_logs, userLogs))

print(mod_userLogs)
