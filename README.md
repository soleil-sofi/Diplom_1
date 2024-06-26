## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Параметризация и моки используются при тестировании класса `Burger`
(в тестах `test_get_receipt_right_ingredients_in_result` и `test_get_price`)

Также используются фикстуры для создания булок, начинок и бургеров

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам (`test_bun.py`, `test_burger.py`, `test_database.py`, `test_ingredient.py`)
- `data_for_tests` - пакет, содержащий тестовые данные

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
