'''
from collections import defaultdict

words = ["кот", "ток", "пёс", "сёп", "кто", "сом"]
anagrams = defaultdict(list)

standard_keys = {
    "".join(sorted("кот")): "кот",
    "".join(sorted("пёс")): "пёс",
    "".join(sorted("сом")): "сом"
}

for word in words:
    
    raw_key = ''.join(sorted(word))

    final_key = standard_keys.get(raw_key, raw_key)
    anagrams[final_key].append(word)

print(dict(anagrams))
'''

users = [
    {"id": 1, "name": "Анна", "email": "a@mail.ru"},
    { "name": "Олег", "email": "o@mail.ru"},
    {"id": 3, "name": "Елена", "email": "e@mail.ru"},
    {"name": "Елена", "email": "e@mail.ru"}
]

#result = {users["id"]: users["name"] for users in users}

resultt = {}
'''
for user in users:

    orig_id = user["id"]
    orig_name = user["name"]
    
    resultt[orig_id] = orig_name
    
print(resultt)
'''
import random
clean_users = {}
un_id = 0

for user in users:
    while un_id not in [u["id"] for u in users]:
        un_id = random.randint(1, 100)
    u_id = user.get("id", f"Unknown {un_id}")
    u_name = user["name"]
    
    clean_users[u_id] = u_name

print(clean_users) 


products = {'хлеб': 35, 'молоко': 80, 'шоколад': 120, 'вода': 40}
products.items()
print(products)

swapped = [(price, name) for name, price in products.items()]

swapped.sort(reverse=True)

final = [(name, price) for price, name in swapped]
print(final)
