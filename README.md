# Проєкт: Трирівнева архітектура

Цей проєкт демонструє повний full-stack додаток, що складається з трьох контейнерів:

1.  **Frontend (Nginx):**
    * Обслуговує статичний `index.html`.
    * Проксіює запити `/api/*` до Backend-сервісу.
    * Доступний за адресою `http://localhost`.

2.  **Backend (Flask):**
    * Надає REST API на `/api/items`.
    * Підключається до бази даних PostgreSQL.

3.  **Database (PostgreSQL):**
    * Зберігає дані.
    * Використовує `volume` з назвою `postgres_data` для збереження стану.

## Запуск

1.  Переконайтеся, що у вас запущено Podman (або Docker).
2.  Виконайте команду у корені проєкту:

    ```bash
    podman compose -f compose.yml up --build
    ```

3.  Відкрийте у браузері `http://localhost`.