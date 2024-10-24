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