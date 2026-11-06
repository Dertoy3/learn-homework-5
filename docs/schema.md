# Требования к модели данных

В базе library_extended создай шесть таблиц в схеме public. Идентификаторы задавай вручную. Таблицы создавай в порядке: readers, authors, categories, books, book_authors, loans.

| Таблица | Поле | Требования |
| --- | --- | --- |
| readers | id | INTEGER, PRIMARY KEY |
| readers | name | TEXT, NOT NULL |
| readers | email | TEXT, UNIQUE, допускает NULL |
| readers | city | TEXT, NOT NULL |
| readers | registered_on | DATE, NOT NULL |
| readers | active | BOOLEAN, NOT NULL, DEFAULT TRUE |
| authors | id | INTEGER, PRIMARY KEY |
| authors | name | TEXT, NOT NULL, имена могут совпадать |
| categories | id | INTEGER, PRIMARY KEY |
| categories | title | TEXT, NOT NULL, UNIQUE |
| books | id | INTEGER, PRIMARY KEY |
| books | title | TEXT, NOT NULL |
| books | category_id | INTEGER, NOT NULL, FOREIGN KEY на categories(id) |
| books | copies | INTEGER, NOT NULL, DEFAULT 0, CHECK >= 0 |
| books | price | NUMERIC(10,2), NOT NULL, CHECK > 0 |
| books | published_year | INTEGER, NOT NULL, CHECK от 1900 до 2026 включительно |
| book_authors | book_id | INTEGER, NOT NULL, FOREIGN KEY на books(id) |
| book_authors | author_id | INTEGER, NOT NULL, FOREIGN KEY на authors(id) |
| loans | id | INTEGER, PRIMARY KEY |
| loans | reader_id | INTEGER, NOT NULL, FOREIGN KEY на readers(id) |
| loans | book_id | INTEGER, NOT NULL, FOREIGN KEY на books(id) |
| loans | loan_date | DATE, NOT NULL |
| loans | due_date | DATE, NOT NULL, CHECK due_date >= loan_date |
| loans | returned | BOOLEAN, NOT NULL, DEFAULT FALSE |
| loans | returned_date | DATE, допускает NULL |

Для book_authors задай составной PRIMARY KEY (book_id, author_id). Одна пара не должна повторяться.

Для loans нужны ещё два CHECK:

- returned_date отсутствует или не раньше loan_date.
- Если returned=FALSE, returned_date должен быть NULL. Если returned=TRUE, returned_date обязателен. Обе части согласуй одним ограничением с AND и OR.

Обязательные поля отдельно защищай NOT NULL: CHECK сам по себе не запрещает NULL. Внешние ключи оставь со стандартным поведением удаления, без CASCADE. По возможности дай ограничениям понятные имена.

Книга может иметь нескольких авторов. У автора пока может не быть книг. Категория пока может быть пустой. Один читатель может брать одну книгу повторно в разные дни: не запрещай повтор пары reader_id/book_id в loans.

copies — количество доступных экземпляров ПОСЛЕ исходных выдач из CSV. Их загрузка не должна ещё раз уменьшать copies. Триггеры и автоматический пересчёт не нужны. Изменение copies при новых выдачах и возвратах выполняй явно в задании 7.

Заблокированный читатель (active=FALSE) может иметь исторические и текущие выдачи: это полезно для отчётов. Прикладные правила вроде запрета новой выдачи такому читателю в этой работе обсуждаются в ответах, а не реализуются через CHECK другой таблицы.
