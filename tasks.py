# Домашнее задание №1

#__Подготовлено__:

#**ФИО**:

#Истомин Владислав Григоьевич

#**ИСУ**:

#471997


#Task 1
def fix_variable_name(variable_name):
    variable_name = variable_name.replace('-', '_')
    new_variable_name = []
    temp_word = ''
    for char in variable_name:
        if char.isupper() and temp_word:
            new_variable_name.append(temp_word.lower())
            temp_word = char
        else:
            temp_word += char
    if temp_word:
        new_variable_name.append(temp_word.lower())

    variable_name = '_'.join(new_variable_name)
    variable_name = variable_name.strip().replace(' ', '_')
    while '__' in variable_name:
        variable_name = variable_name.replace('__', '_')

    while variable_name and variable_name[0].isdigit():
        variable_name = variable_name[1:]

    if not variable_name.isidentifier() or not variable_name:
        return "Введено некорректное имя переменной"

    return variable_name


input_variable = input("Введите имя переменной: ")
result = fix_variable_name(input_variable)
print(result)


def print_products(products):
    print("| ID  | ProductName | Цена |")
    print("|-----|-------------|------|")
    for product in products:
        print(f"| {product['id']} | {product['name']:<11} | {product['price']:>3} |")

#Task 2
def main():
    products = [
        {'id': '001', 'name': 'Батончик', 'price': 70},
        {'id': '002', 'name': 'Вода', 'price': 45},
        {'id': '003', 'name': 'Газировка', 'price': 64},
        {'id': '004', 'name': 'Булочка', 'price': 33}
    ]

    print_products(products)

    product_id = input("Введите ID товара: ").strip()


    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        print("Товара с таким ID не существует")
        return

    remaining_amount = product['price']
    print(f"Внесите {remaining_amount} тугриков")

    while remaining_amount > 0:
        user_input = input("Введите купюру или 'ОТМЕНА' для выхода: ").strip()
        if user_input.upper() == "ОТМЕНА":
            print("Операция отменена")
            return


        try:
            bill = int(user_input)
            if bill not in [10, 50, 100, 500]:
                print("Внесена фальшивая купюра")
                continue

            remaining_amount -= bill

            if remaining_amount < 0:
                print(f"Ваша сдача: {-remaining_amount} тугриков")
                return
            elif remaining_amount == 0:
                print("Ваша сдача: 0 тугриков")
                return
            else:
                print(f"Осталось внести {remaining_amount} тугриков")

        except ValueError:
            print("Внесена фальшивая купюра")
            continue


if __name__ == "__main__":
    main()

#Task 3

person = ['Энакин Скайуокер',
          41,
          ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
          {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
          ]


def main():
    while True:
        task_number = input("Введите номер задания (или 'выход' для выхода): ")

        if task_number.lower() == 'выход':
            break

        if task_number == '1':
            name = person[0].split()
            print(f"Персона: {name[1]}, {name[0]}")
        elif task_number == '2':
            print(person[1])
        elif task_number == '3':
            places = ', '.join(person[2])
            print(places)
        elif task_number == '4':
            print(len(person[2]))
        elif task_number == '5':
            print('Звезда Смерти' in person[2])
        elif task_number == '6':
            print(person[3]['световой меч'])
        elif task_number == '7':
            person[1] = 42
            print(person[1])
        elif task_number == '8':
            new_place = 'Эндор'
            if new_place not in person[2]:
                person[2].append(new_place)
            print(person[2])
        elif task_number == '9':
            rank = person[3]['ранг']
            if rank == 'лорд ситхов':
                print("Энакин - лорд ситхов")
            else:
                print("Энакин - джедай")
        elif task_number == '10':
            if len(person[2]) > 4:
                print("Энакин побывал во многих местах")
            else:
                print("Энакин не так много путешествовал")
        else:
            print("Неверный номер задания")


if __name__ == "__main__":
    main()

#Task 4


companions = ["Astarion", "Gale", "Karlach", "Lae'zel",
              "Shadowheart", "Wyll", "The Dark Urge", "Halsin",
              "Jaheira", "Minsc", "Minthara", "Alfira", "Losiir"]


slice_1 = companions[1:4]
print(slice_1)


slice_2 = companions[1:3] + companions[5:8] + [companions[8], companions[9], companions[11]]  # Halsin дважды, Alfira один раз
print(slice_2)


slice_3 = companions[-1:] + companions[8:9] + companions[5:6] + companions[2:3]
print(slice_3)


slice_4 = companions[0:1] + companions[-1:]
print(slice_4)

#Task5

def main():

    available_items = {'меч', 'лук', 'топор', 'щит', 'зелье'}

    selected_items = [set(), set(), set()]

    for i in range(3):
        while True:

            items_input = input(f"Ввод {i + 1}-го авантюриста (через пробел): ").strip()

            items = set(items_input.split())


            if not items.issubset(available_items):
                print("Неверный предмет, попробуйте снова")
                continue

            if len(items) < 1 or len(items) > 3:
                print("Каждый авантюрист должен выбрать от 1 до 3 предметов")
                continue


            selected_items[i] = items
            break


    common_items = selected_items[0].intersection(selected_items[1], selected_items[2])


    print(len(common_items))




#Task 6

def main():

    x, y = 0, 0



    n = int(input("Введите N: "))


    for i in range(1, n + 1):
        direction = input(f"Ход {i}: ").strip().lower()

        if direction == "вверх":
            y += 1
        elif direction == "вниз":
            y -= 1
        elif direction == "вправо":
            x += 1
        elif direction == "влево":
            x -= 1
        else:
            print("Неверное направление, попробуйте снова.")
            i -= 1


    shortest_distance = abs(x) + abs(y)


    print(shortest_distance)


if __name__ == "__main__":
    main()

#Task 7


def reverse_number(n):
    reversed_number = 0
    negative = n < 0
    n = abs(n)

    while n > 0:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        n //= 10


    return -reversed_number if negative else reversed_number


input_number = int(input("Введите целое число: "))
output_number = reverse_number(input_number)
print(output_number)

#Task 8


song_text = [
    "[Куплет 1]",
    "В истерике кружилась мама Валя",
    "На заднем фоне замер папа Толя",
    "В радиусе метра воцарился жесточайший хаос",
    "Когда всем понятно стало: сын остался без диплома",
    "[Припев]",
    "Я выбираю — жить в кайф!",
    "Я выбираю — жить в кайф!",
    "[Куплет 2]",
    "Слышал я как мимо них ехала такси",
    "[Предприпев 1]",
    "Мама, не кричи, хватит плакать, не смей",
    "[Припев]",
    "Я выбираю — жить в кайф!",
]


song_parts = {
    "куплет 1": [],
    "куплет 2": [],
    "предприпев 1": [],
    "предприпев 2": [],
    "припев": []
}


current_part = None
for line in song_text:
    if "[Куплет 1]" in line:
        current_part = "куплет 1"
    elif "[Куплет 2]" in line:
        current_part = "куплет 2"
    elif "[Предприпев 1]" in line:
        current_part = "предприпев 1"
    elif "[Предприпев 2]" in line:
        current_part = "предприпев 2"
    elif "[Припев]" in line:
        current_part = "припев"
    elif current_part:
        song_parts[current_part].append(line.strip())


def print_part(part_name):
    """Вывод части песни по её названию"""
    if part_name in song_parts:
        print("\n".join(song_parts[part_name]))
    else:
        print("Часть песни не найдена.")


def print_centered_song():
    """Выводит текст песни выровненный по центру без меток."""
    center_width = 80  # Ширина для выравнивания по центру
    for lines in song_parts.values():
        for l in lines:
            if l:
                print(l.center(center_width))


def count_words(input_type):
    """Подсчет самых частых слов."""
    import re
    from collections import Counter


    if input_type == "куплет":
        text_to_analyze = ' '.join(song_parts["куплет 1"] + song_parts["куплет 2"])
    elif input_type == "песня":
        text_to_analyze = ' '.join([' '.join(lines) for lines in song_parts.values()])
    else:
        return


    text_to_analyze = text_to_analyze.lower()
    text_to_analyze = re.sub(r'[^a-zа-яё0-9\- ]+', '', text_to_analyze)  # Удаление специальных символов
    words = text_to_analyze.split()


    word_counts = Counter(words)

    most_common = word_counts.most_common(3)


    for index, (word, count) in enumerate(most_common, start=1):
        print(f"{index}. \"{word}\" - {count} раз")


def main():
    while True:
        user_input = input("Введите номер задания (1, 2, 3) или 'выход': ").strip().lower()

        if user_input == "выход":
            break

        if user_input == "1":
            part_name = input("Введите название элемента песни (например, 'припев'): ").strip().lower()
            print_part(part_name)

        elif user_input == "2":
            print_centered_song()

        elif user_input == "3":
            song_type = input("Введите 'куплет' или 'песня': ").strip().lower()
            count_words(song_type)


if __name__ == "__main__":
    main()