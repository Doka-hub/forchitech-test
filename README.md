Тестовое задание для Forchitech
==============================
### Задание
Написать микросервис, который будет выводить информацию по адресу в сети трон, его bandwidth, energy, и баланс trx, ендпоинт должен принимать входные данные - адрес.
Каждый запрос писать в базу данных, с полями о том какой кошелек запрашивался.
Написать юнит/интеграционные тесты

У сервиса 2 ендпоинта
- POST
- GET для получения списка последних записей из БД, включая пагинацию,

2 теста
- интеграционный на ендпоинт
- юнит на запись в бд

Примечания: использовать FastAPI, аннотацию(typing), SQLAlchemy ORM, для удобства с взаимодействию с троном можно использовать tronpy, для тестов Pytest

### Quickstart
1. Запуск докера
```bash
docker compose up --build -d
```
2. Запуск тестов
```bash
docker compose run -rm tests
```
