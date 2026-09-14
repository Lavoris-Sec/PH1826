# class SimpleClass:
#     pass
#
#
# simple_class_obj = SimpleClass()
#
# print(simple_class_obj)
# print(type(simple_class_obj))
#
# print(isinstance(simple_class_obj, SimpleClass))

stack_list = []


def push(element):
    stack_list.append(element)
    print(stack_list)


def pop():
    if len(stack_list) > 0:
        removed = stack_list[-1]
        del stack_list[-1]
        return removed


push(3)
push(2)
push(1)
print("-----")
print(pop())
print(pop())
print(pop())
