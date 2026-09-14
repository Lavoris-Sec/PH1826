myNumbers=['12.3','-12','45.67','+30', '-11']

first_digits = list(map(lambda x: int(x.lstrip('+-')[0]), myNumbers))

print(first_digits)