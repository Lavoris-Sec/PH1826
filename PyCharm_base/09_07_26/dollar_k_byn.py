bun_to_dollar = 2.86
discount = 0.15

calculate_price = lambda p: p / bun_to_dollar  # Цена без скидки
calculate_with_d = lambda p: (p / bun_to_dollar) * (1 - discount)  # Цена со скидкой
calculate_discount = lambda p: (p / bun_to_dollar) * discount  # Размер скидки

price_one = float(input("Введите цену первого товара: "))

print("\n--- Товар 1 ---")
print(f"Итого со скидкой: ${calculate_with_d(price_one):.2f}")
print(f"Итого без скидки: ${calculate_price(price_one):.2f}")
print(f"Размер скидки ({discount * 100}%): ${calculate_discount(price_one):.2f}")

price_two = float(input("Введите цену второго товара: "))

print("\n--- Товар 2 ---")
print(f"Итого со скидкой: ${calculate_with_d(price_two):.2f}")
print(f"Итого без скидки: ${calculate_price(price_two):.2f}")
print(f"Размер скидки ({discount * 100}%): ${calculate_discount(price_two):.2f}")
