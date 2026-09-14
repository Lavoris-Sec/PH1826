'''
me = {1, True, 0, False}
print(me)
my = {True, 1, False, 0}
print(my)
if 0 is False:
    print('1')
fs = frozenset([1, 2, 2, 3])
fs.add(4)
print(fs)

'''

my_dict = {1:5, '2':7}
my_dict
print(my_dict)

students = ["Анна", "Олег", "Мария", "Fish"]
grades = [5, 4]

result = dict(zip(students, grades))
'''
result_s = {name: grade for name, grade in zip(students, grades)}

result_t = {}
for i in range(len(students)):
    result_t[students[i]] = grades[i]
'''
'''
rrresult = {
    students[i]: (grades[i] if i < len(grades) else "") 
    for i in range(len(students))
}

resultt = {}
for i in range(len(students)):
    name = students[i]
    
    if i < len(grades):
        value = grades[i]
    else:
        value = "" 
    
    resultt[name] = value


print(result)
print(result_s)
print(result_t)

print(resultt)
f = resultt.values()
print(hash(None))
'''

check = result.values()
print(check)
