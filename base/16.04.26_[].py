import copy
'''
me = [1,8,5,8,5,9,[4,5]]
print(me)
cme = me[:]
print(cme)
deep_copy_list = copy.deepcopy(me)
me[-1].append(4)
print(deep.copy_list)
print(me,'\n',cme)


my_list = [5,8,2,6,9,[4,5]]
my_list[-1]=my_list[-1]+[6]
print([4,5]+[6])
print(my_list)
deep_copy_list = copy.deepcopy(my_list)
print(deep_copy_list)
#print(me)
#print(cme)

'''

#Task1
'''
my_list = [5, 4, 8, 9, 3]
print(my_list[0])
print(my_list[-1])
print(len(my_list))
our_sum = 0
for index in my_list:
    our_sum += index

print(our_sum)
'''

#Task2
'''
colors = ["red", "green", "blue", "yellow", "purple"]

colors[colors.index('blue')] = 'cyan'

colors.append('magenta')
colors.insert(2, 'orange')
colors.remove('yellow')
print(colors.pop(-1))
print(colors)
'''

#Task3
'''
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[0:3])
print(nums[2:6])
print(nums[::2])
print(nums[::-1])
'''

#Task4
'''
sl = [3, 7, 5, 10, 4]
min_s = sl[0]
max_s = 0
for number in sl:
    if number > max_s:
        max_s = number
    if number < min_s:
        min_s = number

print('Максимальный символ - ', max_s)
print('Минимальный символ  - ', min_s)
'''

#Task5

import random

# Параметры: (откуда, k=сколько штук)
#sl = random.choices(range(-5, 10), k=10)
# или

# Параметры: (откуда выбираем, сколько штук)
#sl = random.sample(range(1, 100), 10) 
#print(sl)
'''

#sl = [2, 5, 8, 3, 10]
count_p = 0
count_n = 0
for num in sl:
    if num % 2 == 0:
        count_p += 1
    if num % 2 == 1:
        count_n += 1

print('Кол-во четных - ', count_p)
print('Кол-во нечетных - ', count_n)
if count_p > count_n:
    print('Четных чисел больше')
elif count_n > count_p:
    print('Нечетных больше')
else:
    print('Кол-во равно')
'''

#Task6
'''
listt = [1, 3, 2, 3, 1, 4]
sort_list = []

for num in sl:
    if num not in sort_list:
       sort_list.append(num)

print(sort_list)
'''


#Task7
'''
import random

for count in range(10000):
    object_ = random.choices(range(0, 20), k=1000)
    min_s = object_[0]
    max_s = object_[0]
    
    for number in range(10000):
        if number > max_s:
            max_s = number
        if number < min_s:
            min_s = number
    
    true_max = max(object_)
    true_min = min(object_)
    
    if max_s != true_max or min_s != true_min:
        print('Наш метод\tmax -', max_s, '\tmin -', min_s)
        print('Машинный метод\tmax -', true_max, '\tmin -', true_min)
        break
else:
    print("Все тесты прошли успешно!")
'''

#Task8
'''
string = ["hi", "hello", "a", "world", "bebe", '123']
filter_list = []

for s in string:
    if len(s) > 3:
        filter_list.append(s)

print(filter_list)
'''

#Task9
'''
string1 = [1, 2, 3]
string2 = ["a", "b", "c"]

new_string = []

for char in range(len(string1)):
    new_string.append([string1[char], string2[char]])
print(new_string)
'''

#Task10
'''
string1 = [1, 2, 3]
string2 = ["a", "b", "c", "d", "e"]

new_list = []

general_length = len(string1)

if general_length > len(string2):
    general_length = len(string2)
  
for i in range(general_length):
    new_list.append(string1[i])
    new_list.append(string2[i])

new_list += string1[general_length:]
new_list += string2[general_length:]

print(new_list)
'''

#Task11
'''
matrix = [[1,2,3], [4,5,6], [7,8,9]]

sum_m = []

for i in matrix:
    s = 0
    for num in i:
        s += num
    sum_m.append(s)
print("Суммы:" ,sum_m)
'''

#Task12
'''
matrix = [[1,2],[3,4]]
n = len(matrix)

new_matrix = []
for i in range(n):
    new_matrix.append([0] * n)

for i in range(n):
    for j in range(n):
        new_matrix[j][i] = matrix[i][j]
        
for row in new_matrix:
    print(row)
'''

num_list = []

for i in range(10):
    if i % 2 == 0:
        num_list.append(i)
    elif i == 3:
        num_list.append(i)

print(num_list)

num_list = [i for i in range(10) if i % 2 == 0 or i == 3]

print(num_list)
