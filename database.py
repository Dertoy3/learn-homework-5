"""Задание 11.1: подключение к PostgreSQL. Условия в docs/python-tasks.md."""


def connect():
    """Верни новое открытое соединение Psycopg с autocommit=False.

    Прочитай PGHOST, PGPORT, PGDATABASE, PGUSER из окружения.
    По умолчанию: localhost, 5432, library_extended, postgres.
    Пароль запроси через getpass.getpass при каждом вызове.
    Здесь соединение не закрывай: вызывающая функция использует with connect().
    """
    raise NotImplementedError("Реализуй database.connect()")
