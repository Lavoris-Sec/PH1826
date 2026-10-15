'''
s = "example"
result = [char + "*" for char in s]
print(result)


str_ = "abcdtf"
result = [char * 5 for char in str_]
print(result)


sq = []

for x in range(1, 11):
    if x % 2 == 0:
        sq.append(x**2)

print(sq)

import pprint

matrix = [[i * j for j in range(1, 11)] for i in range(1, 10)]


for index in matrix:
    print(index)


print(*matrix, sep = '\n')

'''
'''
for i in range(1, 11):
    for j in range(1, 11):

        print(i * j, end="\t")
    print() 
'''
'''
modify = [[print(i * j, end = '\t' if j < 10 else '\n') for j in range(1, 11)] for i in range(1, 10)]
'''


'''
[print([i * j for j in range(1, 11)]) for i in range(1, 10)]
'''

'''
customers=['Bob','Anna','Joe','Bob','Nick']
different = []

for name in customers:
    if name not in ['Bob', 'Joe']:
        different.append(name)
print(different)
'''



bebe = 1, 2, 3, 

#palindrome = bebe == bebe[::-1]

#print(palindrome)
bebe = tuple(bebe)
print(type(bebe))
#print(hash(bebe))

bebe = list(bebe)
print(type(bebe))

var1, var2, var3 = 1, 2, 3
print(var1, var2, var3)
