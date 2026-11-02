"""Дополнительное задание. Условия подключения и запроса смотри в README."""


def find_reader(reader_id):
    """Верни имя читателя по id или None, если его нет.

    Подключение: PGHOST, PGPORT, PGDATABASE, PGUSER из окружения.
    Значения по умолчанию: localhost, 5432, library, postgres.
    Пароль запроси через getpass.getpass.
    Используй Psycopg, параметр %s и контекстный менеджер соединения.
    Ошибки подключения и SQL не подменяй значением None.
    """
    raise NotImplementedError("Реализуй find_reader(reader_id)")
