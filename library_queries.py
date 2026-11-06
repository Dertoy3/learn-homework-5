"""Задания 11.3–11.5: чтение и добавление читателей через Psycopg."""


def available_books(min_copies=1):
    """Верни список кортежей (id, title, copies, price).

    Условие copies >= min_copies. Порядок по copies DESC, затем id ASC.
    min_copies — целое число >= 1; иначе ValueError до подключения.
    Используй параметризованный запрос и with database.connect().
    Если книг нет, верни [].
    """
    raise NotImplementedError("Реализуй available_books(min_copies)")


def reader_loans(reader_id):
    """Верни текущие выдачи читателя: [(loan_id, title, due_date), ...].

    Используй JOIN с books, returned=FALSE и отдельный параметр reader_id.
    Порядок по due_date, затем loans.id. Даты верни как datetime.date.
    При отсутствии читателя или выдач верни []. Не печатай внутри функции.
    """
    raise NotImplementedError("Реализуй reader_loans(reader_id)")


def add_reader(reader_id, name, email, city, registered_on):
    """Добавь активного читателя и верни reader_id после подтверждения.

    registered_on — datetime.date. Пустой email передай как None.
    Не меняй существующую строку при повторном id или email.
    Подключение через database.connect(), все значения — отдельные параметры.
    Ошибки PostgreSQL передай вызывающему коду. Соединение должно закрыться.
    """
    raise NotImplementedError("Реализуй add_reader(...)")
