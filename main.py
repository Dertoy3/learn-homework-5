"""Готовый запуск дополнительного задания: python main.py."""

from find_reader import find_reader


def main():
    try:
        reader_id = int(input("Введите id читателя: "))
    except ValueError:
        print("id должен быть целым числом")
        return

    try:
        name = find_reader(reader_id)
    except NotImplementedError as error:
        print(error)
        return

    if name is None:
        print("Читатель не найден")
    else:
        print(f"Читатель: {name}")


if __name__ == "__main__":
    main()
