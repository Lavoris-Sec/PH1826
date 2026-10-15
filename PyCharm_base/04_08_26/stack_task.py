stack_list = ["([{})][()(){}]"]

check_list = []

db_open = ["(", "{", "["]
db_close = [")", "}", "]"]


def push(el):
    check_list.append(el)
    print(check_list)


def pop():
    if len(stack_list) > 0:
        removed = stack_list[-1]
        del stack_list[-1]
        return removed


for element in stack_list:
    if element in db_open:
        push(element.split())
