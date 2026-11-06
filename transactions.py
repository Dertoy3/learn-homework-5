"""Две обязательные транзакции Python. Полные условия в docs/python-tasks.md."""


def issue_book(loan_id, reader_id, book_id, loan_date, due_date,
               *, fail_after_update=False):
    """Выдай книгу: уменьшение copies и INSERT loans в одной транзакции.

    Даты — datetime.date. При успехе верни loan_id после подтверждения.
    Нет читателя/он заблокирован, нет доступной книги или некорректный
    порядок дат: ValueError. Ошибки драйвера, включая повтор id, не скрывай.
    Уменьшай copies только при copies>0; проверь число изменённых строк.
    Если fail_after_update=True, после уменьшения copies, ДО INSERT,
    подними RuntimeError("Учебная ошибка выдачи"). Изменения откатываются.
    Используй одно соединение, autocommit=False и with для всей операции.
    """
    raise NotImplementedError("Реализуй транзакцию issue_book(...)")


def return_book(loan_id, returned_on, *, fail_after_update=False):
    """Верни книгу: закрытие выдачи и увеличение copies в одной транзакции.

    returned_on — datetime.date. При успехе верни book_id после подтверждения.
    Закрывай только открытую выдачу, получи book_id через UPDATE ... RETURNING.
    Нет строки результата (не найдена/уже закрыта): ValueError.
    Дата раньше loan_date: ошибка CHECK PostgreSQL, передай её наружу.
    Если fail_after_update=True, после закрытия выдачи, ДО увеличения copies,
    подними RuntimeError("Учебная ошибка возврата"). Откатываются обе части.
    Повторный возврат не должен увеличивать copies второй раз.
    Используй одно соединение, autocommit=False и with для всей операции.
    """
    raise NotImplementedError("Реализуй транзакцию return_book(...)")
