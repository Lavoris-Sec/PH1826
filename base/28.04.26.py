'''
print(hash('Саня'))
print(hash('Аня'))
print(hash('Ника'))

print(hash(5524708964097617990))
my_tuple = (1, 2, '3', 'A', [7, 9], 2, False, None)
print(my_tuple)
for i in my_tuple:
    print(id(i))
my_tuple[4].append(5)
print('====================================')
print(my_tuple)
for i in my_tuple:
    print(id(i))
'''
'''
my_tuple = (11, 12, 13, 14, 15)

print(my_tuple[0])
print(my_tuple[-1])
print(len(my_tuple))
s = 0
for i in my_tuple:
    s += i
print(s)
'''
'''
my_tuple = (42, 3.14, "Привет, мир!", True, [])

print(my_tuple)

length = len(my_tuple)
print(length)
'''
'''
numbers = (10, 20, 30, 40, 50, 60, 70, 80)
print(numbers[0], numbers[-1])
new_tuple = numbers[2:6]
print(new_tuple)
print(numbers[1::2])
'''
'''
person = ("Анна", 28, "инженер")

name = person[0]
age = person[1]
profession = person[2] + 'ом'

print(f'{name} работает {profession} и ей {age} лет')
'''
'''
a = 5
b = 12

a = a + b
b = a - b
a = a - b
print(f'a = {a}, b = {b}')
'''
'''
grades = (4, 5, 4, 3, 5, 5, 4, 3, 5, 4, 5)

count = 0
c3 = 0
for i in grades:
    if i == 5:
        count += 1

count_5 = grades.count(5)

print(f'{count} учеников получили 5 \t Для сравнения {count_5}')

first_3 = grades.index(3)
print(first_3)

first_5 = grades.index(5,3)
print(first_5)
'''

players = [("Иван", 2500), ("Мария", 3200), ("Петр", 1800), ("Алиса", 2900)]

temp = []
final = []

for name, score in players:
    temp.append((score, name))
    
temp.sort()
temp = temp[::-1]

for score, name in temp[:3]:  
    final.append((name, score))

print(f'Топ-3 {final}')



cities = ["Москва", "Лондон", "Токио"]

my_tuple = tuple(cities)

print(f"Исходник - {my_tuple}")

temp = list(my_tuple) 
temp.append("Париж")        
my_tuple = tuple(temp) 
print(f"Обновление - {my_tuple}")

print(f"Исходный список - {cities}")


names = ["Alice", "Bob"]
scores = [85, 92]

result = list(zip(names, scores))
print(type(zip(names)))
'''
tlist = list(1,)

tulist = tuple(tlist)
print(type(tulist))
'''

values = (100, 200, 300, 400, 500)

first, *middle, end = values

print(first, middle, end)

'''
my_t = (1, 2) + (3, 4)
a, b, *c = my_t
print(a, b)
'''
