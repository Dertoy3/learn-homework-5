-- 9. Отладка: найди и исправь шесть ошибок
-- Подробный порядок выполнения: README.md. Требования к полям: docs/schema.md.

-- 1. Запрос 9.1 ниже должен находить читателей без email. Исправь и объясни ошибку.
-- TODO: напиши решение здесь.

-- 2. Запрос 9.2 ниже должен выводить выдачи с именами читателей. Исправь связь, сохрани SELECT и JOIN.
-- TODO: напиши решение здесь.

-- 3. Запрос 9.3 ниже должен сохранять всех читателей, даже без текущих выдач. Исправь расположение фильтра.
-- TODO: напиши решение здесь.

-- 4. Запрос 9.4 ниже должен менять город только читателя 3. Добавь безопасное условие и покажи строку до/после. Выполняй исправление внутри BEGIN/ROLLBACK.
-- TODO: напиши решение здесь.

-- 5. Запрос 9.5 ниже должен создавать категорию. Исправь синтаксис, выполни внутри BEGIN/ROLLBACK.
-- TODO: напиши решение здесь.

-- 6. Запрос 9.6 ниже должен создавать незакрытую выдачу с корректными датами. Исправь только значения дат, выполни внутри BEGIN/ROLLBACK. Для этого упражнения copies не меняй: здесь проверяется ограничение дат.
-- TODO: напиши решение здесь.


-- Неверные примеры ниже закомментированы. Рядом напиши исправления.
-- Каждый новый SELECT располагай под соответствующим условием выше.

-- 9.1 SELECT id, name FROM public.readers WHERE email = NULL;

-- 9.2 SELECT l.id, r.name FROM public.loans l
--     JOIN public.readers r ON r.id = l.id;

-- 9.3 SELECT r.id, r.name, l.id AS loan_id
--     FROM public.readers r LEFT JOIN public.loans l ON l.reader_id = r.id
--     WHERE l.returned = FALSE;

-- 9.4 UPDATE public.readers SET city = 'Тула';

-- 9.5 CREATE TABLE public.debug_categories (
--         id INTEGER PRIMARY KEY
--         title TEXT NOT NULL
--     );

-- 9.6 INSERT INTO public.loans
--     (id, reader_id, book_id, loan_date, due_date, returned)
--     VALUES (950, 3, 10, DATE '2026-06-10', DATE '2026-06-01', FALSE);
