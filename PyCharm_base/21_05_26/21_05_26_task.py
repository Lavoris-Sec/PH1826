def greeting(customers_list_orig, customers_list_mod):

    for customer in range(len(customers_list_mod)):
        element_mod = customers_list_mod[customer]
        element_orig = customers_list_orig[customer]
        if 'admin' in element_mod:
            print(f'Добрый день {element_orig} - admin')
        elif 'student' in element_mod:
            print(f'Привет {element_orig} - student')
        else:
            print(f'Даров {element_orig}')


def lower_maker(customers_list):
    customers_list_mod = []
    for customer in customers_list:
        customers_list_mod.append(customer.lower())

    return customers_list_mod

customers=['AdminJane', 'adminBob', 'STUDENTbob',  'studentAlice', 'Kate']

mod_list = lower_maker(customers)

greeting(customers, mod_list)