'''
my_set = set()
print(type(my_set))
my_list = []
my_set = set(my_list)
print(type(my_set))
print(my_set, my_list)
'''

'''
sset = {'1', '2', '3'}
print(hash('1'), ' = 1')
print(hash('2'), ' = 2')
print(hash('3'), ' = 3')
my_list = [hash('1'), hash('2'), hash('3')]
my_list.sort
print(my_list)
print(sset)
'''
'''
my_set = {1, 2, 3, 1, 3, 2, True, False}
my_set.discard(2)
print(my_set)



s = {1,2,3}
s.remove(2)    
#s.remove(1)    

s.discard(10) 
print(s.pop())
fg = frozenset([11])
fs = frozenset([1, 2, 3, fg])

print(hash(fs))
print(fs)
print(type(fs))
'''

'''
data = [1, 2, 2, 3, 3, 3, 4]
s = set(data)
print(s)
'''

'''
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))              
print(A.intersection(B))       
print(A.difference(B))         
print(A.symmetric_difference(B))
'''

'''
s = {1, 2, 3}
s.add(2)
print(s)
'''
'''
my_set = {1, 2, 3, 4, 5}
print(my_set.issuperset([1, 2, 3]))
print(my_set >= {1,2,3})
print(all(item in my_set for item in [1, 2, 3]))


sett = {1, 10, 2}
sett.discard(10)
print(sett)


list1 = [1,2,2,3]
list2 = [2,3,4]

result = set(list1).intersection(list2)
print(list(result))


A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))              
print(A.intersection(B))       
print(A.difference(B))         
print(A.symmetric_difference(B))
'''

'''
s = {1, 2, 3}
s.update([3, 4, 5])
print(s)
'''

my_set = [3, 2, 1, 2, 3, 4]


result = list(dict.fromkeys(my_set))

print(result)
