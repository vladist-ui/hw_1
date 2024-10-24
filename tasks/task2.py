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