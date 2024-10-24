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