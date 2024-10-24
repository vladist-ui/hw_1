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