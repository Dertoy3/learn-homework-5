"""Готовое меню обязательного Python-блока: python main.py."""

from datetime import date

from find_reader import find_reader
from library_queries import add_reader, available_books, reader_loans
from transactions import issue_book, return_book


def ask_int(prompt):
    return int(input(prompt))


def ask_date(prompt):
    return date.fromisoformat(input(prompt).strip())


def show_rows(rows):
    if not rows:
        print("Записей нет")
        return
    for row in rows:
        print(" | ".join(str(value) for value in row))


def issue_action(fail=False):
    loan_id = issue_book(
        ask_int("id новой выдачи: "),
        ask_int("id читателя: "),
        ask_int("id книги: "),
        ask_date("Дата выдачи YYYY-MM-DD: "),
        ask_date("Срок возврата YYYY-MM-DD: "),
        fail_after_update=fail,
    )
    print(f"Выдача сохранена: {loan_id}")


def return_action(fail=False):
    book_id = return_book(
        ask_int("id выдачи: "),
        ask_date("Дата возврата YYYY-MM-DD: "),
        fail_after_update=fail,
    )
    print(f"Возврат сохранён, id книги: {book_id}")


def run_action(choice):
    if choice == "1":
        name = find_reader(ask_int("id читателя: "))
        print("Читатель не найден" if name is None else f"Читатель: {name}")
    elif choice == "2":
        show_rows(available_books(ask_int("Минимум доступных экземпляров: ")))
    elif choice == "3":
        show_rows(reader_loans(ask_int("id читателя: ")))
    elif choice == "4":
        reader_id = add_reader(
            ask_int("id нового читателя: "),
            input("Имя: ").strip(),
            input("Email (Enter, если нет): ").strip() or None,
            input("Город: ").strip(),
            ask_date("Дата регистрации YYYY-MM-DD: "),
        )
        print(f"Читатель добавлен: {reader_id}")
    elif choice in ("5", "7"):
        issue_action(fail=choice == "7")
    elif choice in ("6", "8"):
        return_action(fail=choice == "8")
    else:
        print("Выбери пункт от 0 до 8")


def main():
    try:
        import psycopg
    except ImportError:
        print("Установи зависимости: python -m pip install -r requirements.txt")
        return

    while True:
        print("\n1 — Найти читателя\n2 — Доступные книги\n3 — Выдачи читателя"
              "\n4 — Добавить читателя\n5 — Выдать книгу (транзакция 1)"
              "\n6 — Вернуть книгу (транзакция 2)"
              "\n7 — Выдать с учебной ошибкой\n8 — Вернуть с учебной ошибкой"
              "\n0 — Выход")
        choice = input("Выбор: ").strip()
        if choice == "0":
            return
        try:
            run_action(choice)
        except NotImplementedError as error:
            print(f"Заготовка: {error}")
        except ValueError as error:
            print(f"Проверь ввод или условия операции: {error}")
        except RuntimeError as error:
            print(f"Учебная ошибка: {error}. Проверь состояние базы.")
        except psycopg.Error as error:
            print(f"PostgreSQL [{error.sqlstate or 'подключение'}]: {error}")


if __name__ == "__main__":
    main()
