# Служба управления заметками

Это простой сервис REST API для управления заметками с функцией проверки правописания и базовой аутентификацией.

## Функции
- Управление заметками (CRUD)
- Проверка орфографии заметки с помощью API Яндекс.Спеллера.
- Базовая аутентификация с предварительно настроенными пользователями.
- JSON-хранилище для заметок
- Докеризован для развертывания.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Slimpush/kode_testwork.git
    cd kode_testwork
    ```

2. Создайте виртуальную среду и активируйте ее:
    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустите приложение:
    ```bash
    uvicorn notes.main:app --reload
    ```

5. API будет доступен по адресу http://127.0.0.1:8000.

## Использование

### Аутентификация
Служба использует базовую аутентификацию. Используйте следующие учетные данные:
- Имя пользователя: `user1`, пароль: `Pwtest1`
- Имя пользователя: `user2`, пароль: `Pwtest2`

### Эндпоинты

- **POST/notes/**: добавить новую заметку
- **GET /notes/**: получить все заметки для аутентифицированного пользователя


## В папке data хранится экспортированная Postman коллекция для проверки.
