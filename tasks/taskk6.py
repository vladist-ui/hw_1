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