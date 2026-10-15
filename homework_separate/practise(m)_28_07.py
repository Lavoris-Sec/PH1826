import time


def check_meat_safety(meat_type, roasting):
    meat = meat_type.lower()
    style = roasting.lower()

    if ("кур" in meat or "рыб" in meat) and style != "well done":
        return roasting, True

    return roasting, False


def topping_add(u_or_b):
    if u_or_b == 0:
        position = "над"
    if u_or_b == 1:
        position = "под"

    toppings = ["Бекон - 🥓 🥓 🥓\n", "Помидор - 🍅 🍅 🍅\n", "Соленый огурец - 🥒 🥒 🥒\n", "Лук - 🧅 🧅 🧅\n",
                "Сыр - 🧀 🧀 🧀\n", "Лист салата - 🥬 🥬 🥬\n"]
    logo = ["🥓", "🍅", "🥒", "🧅", "🧀", "🥬"]

    chosen_toppings = []
    ready_logos = []

    time.sleep(0.7)

    print("\n--- ДОСТУПНЫЕ НАЧИНКИ ---")
    print("1:", toppings[0])
    print("2:", toppings[1])
    print("3:", toppings[2])
    print("4:", toppings[3])
    print("5:", toppings[4])
    print("6:", toppings[5])

    user_input = input(
        f"\nВведите номера начинок {position} котлетой(в случае если доп. начинка не нужна, просто нажмите Enter): ")

    split_input_up = user_input.split()

    for num in user_input:
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(toppings):
                chosen_toppings.append(toppings[index])
                ready_logos.append(logo[index])
            else:
                print("Был введен неверный номер, элемент будет пропущен")

    for topping in chosen_toppings:
        print(f"{topping}")

    return ready_logos


def burger_decorator(meatFunction):
    def simpleWrapper(meat_type, roasting):

        safe_roasting, was_changed = check_meat_safety(meat_type, roasting)

        icon_meat = meat_type.lower()

        bun_top = "⌒⌒⌒"
        bun_bottom = "◡◡◡"

        if was_changed and "кур" in meat_type.lower():
            print(f"⚠ ☠ ⚠ Внимание: Курицу с прожаркой '{roasting}' употреблять опасно!⚠ ☠ ⚠")
            print("Рекомендуем перед употреблением узнать действительна ли ваша мед страховка!")
            prefix = "ЧИКЕН"
        elif was_changed and "рыб" in meat_type.lower():
            print(f"⚠ ☠ ⚠ Внимание: Рыбу с прожаркой '{roasting}' употреблять опасно!⚠ ☠ ⚠")
            print("Рекомендуем перед употреблением узнать действительна ли ваша мед страховка!")
            prefix = "ФИШ"
        elif "говя" in meat_type:
            prefix = "ГАМ"
        elif "бара" in meat_type:
            prefix = "ЛАМ"
        else:
            prefix = ""

        time.sleep(0.9)

        print(f"\n=== НАЧИНАЕМ СБОРКУ {prefix}БУРГЕРА ===")
        print("⌒ - Верхняя булочка")

        top_toppings_logos = topping_add(0)
        time.sleep(0.8)
        print("---------------------------------")

        meat_result = meatFunction(meat_type, safe_roasting)

        print("♨️")
        print(
            "🐔" if "кур" in icon_meat else "🐟" if "рыб" in icon_meat else "🐮" if "говя" in icon_meat else "🐏" if "бара" in icon_meat else "🥩")
        print("🍳")
        print("🔥")

        print("---------------------------------")

        time.sleep(1)

        bottom_toppings_logos = topping_add(1)

        print("◡ - Нижняя булочка")

        if "кури" in meat_type.lower():
            print("=== ЧИКЕНБУРГЕР ГОТОВ ===")
        elif "рыб" in meat_type.lower():
            print("=== ФИШБУРГЕР ГОТОВ ===")
        elif "говя" in meat_type.lower():
            print("=== ГАМБУРГЕР ГОТОВ ===")
        else:
            print("=== БУРГЕР ГОТОВ! ===")

        print(f"   {bun_top}   ")

        for l in top_toppings_logos:
            print(f" {l} {l} {l} ")

        meat_icon = "🐔" if "кур" in icon_meat else "🐟" if "рыб" in icon_meat else "🐮" if "говя" in icon_meat else "🐏" if "бара" in icon_meat else "🥩 "
        print(f"({meat_icon} - {safe_roasting})")

        for l in bottom_toppings_logos:
            print(f" {l} {l} {l} ")
            time.sleep(0.5)

        print(f"   {bun_bottom}  ")
        print("=====================\n")

        return meat_result

    return simpleWrapper


@burger_decorator
def makeCutlet(meat_type, roasting):
    print(f"Жарим котлету из {meat_type} ({roasting})")
    return f"Котлета ({meat_type})"


print("--- ЗАКАЗ №1 (Опасная курица) ---")
order_1 = makeCutlet("Куриное филе", "Medium Rare")
time.sleep(5)

print("\n--- ЗАКАЗ №2 (Правильная говядина) ---")
order_2 = makeCutlet("Мраморная говядина", "Medium")
time.sleep(5)

print("\n--- ЗАКАЗ №3 (рыба не та) ---")
order_3 = makeCutlet("Рыба", "rare")
time.sleep(5)

print("\n--- ЗАКАЗ №4 (баранина) ---")
order_4 = makeCutlet("Баранина", "Ultra rare")
time.sleep(5)
