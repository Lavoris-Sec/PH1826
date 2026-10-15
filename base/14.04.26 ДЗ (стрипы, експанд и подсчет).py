#Емае
'''
text = "программирование на питоне"
vowels_ref = "аеёиоуыэюяaeiouy"
consonants_ref = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"

v_count = 0
c_count = 0


chars = "" 
counts = [] 

for char in text.lower():
    is_vowel = False
    for v in vowels_ref:
        if char == v:
            is_vowel = True
    
    if is_vowel:
        v_count += 1
    else:
        is_consonant = False
        for c in consonants_ref:
            if char == c:
                is_consonant = True
        if is_consonant:
            c_count += 1


    if char != " ":
        found_idx = -1

        for i in range(len(chars)):
            if chars[i] == char:
                found_idx = i
        
        if found_idx == -1:
            chars += char    
            counts.append(1)  
        else:
            counts[found_idx] += 1


max_val = 0
most_freq_char = ""
for i in range(len(counts)):
    if counts[i] > max_val:
        max_val = counts[i]
        most_freq_char = chars[i]

print("Гласных:", v_count)
print("Согласных:", c_count)
print("Самый частый символ:", most_freq_char, "(", max_val, "раз)")
'''

#Expandtabs
'''
tabbed_str = "Имя\tВозраст\tГород"
clean_str = ""

for char in tabbed_str:
    if char == "\t":
        clean_str += "    " 
    else:
        clean_str += char

print(clean_str)
'''

#Таблица умножения(правильная)
'''
for i in range(1, 11):
    line = ""
    for j in range(1, 11):
        res = i * j
        
        s_res = str(res)
        
        while len(s_res) < 4:
            s_res += " "
            
        line += s_res
    
    print(line)
'''

print(' ',' ',sep='\n',end='\n')

#Таблица умножения(неправильная)
'''
for index in range(1, 11):
    line = ""
    for jj in range(2, 6):
        res = jj * index
        part = str(jj) + " * " + str(index) + " = " + str(res)
        while len(part) < 15:
            part += " "
        line += part
    print(line)

print()

for index in range(1, 11):
    line = ""
    for jj in range(6, 10):
        res = jj * index
        part = str(jj) + " * " + str(index) + " = " + str(res)
        while len(part) < 15:
            part += " "
        line += part
    print(line)
'''

#Lstrip
'''
s = "   привет мир   "

start = 0
while start < len(s) and s[start] == " ":
    start += 1

lstripped = s[start:]
print(lstripped) 
'''

#Rstrip
'''
mystrR = "   привет мир   "
end = len(mystrR) - 1
while end >= 0 and mystrR[end] == " ":
    end -= 1

rstripped = mystrR[:end + 1]

print(rstripped) 
'''

#Strip
'''
strip = "   привет мир   "

start = 0
while start < len(strip) and strip[start] == " ":
    start += 1

end = len(strip) - 1
while end >= start and strip[end] == " ":
    end -= 1

full_stripped = strip[start:end + 1]

print(full_stripped) 
'''


