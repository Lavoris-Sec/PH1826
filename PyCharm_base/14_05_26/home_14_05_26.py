#Математически отзеркалить 12345, чтобы получилось 54321, а затем его вернуть в исходное


num = 100000
original = num
print("Исходное:", num)

temp = num
digit_count = 0
while temp > 0:
    digit_count += 1
    temp //= 10
if original == 0:
    digit_count = 1


num_temp = num
revers_num = 0
while num_temp > 0:
    revers_num = revers_num * 10 + (num_temp % 10)
    num_temp //= 10


print("Отзеркаленное: ", end="")
for i in range(digit_count - 1, -1, -1):
    divisor = 1
    for _ in range(i):
        divisor *= 10
    digit = (revers_num // divisor) % 10
    print(digit, end="")
print()

restored_num = revers_num

temp_rc = revers_num
rc_digits = 0
if temp_rc == 0:
    rc_digits = 1
else:
    while temp_rc > 0:
        rc_digits += 1
        temp_rc //= 10

for _ in range(digit_count - rc_digits):
    restored_num *= 10

print("Восстановленное:", restored_num)


