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