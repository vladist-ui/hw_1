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