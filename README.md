## Задача

Описано в файле tz.docx

Разработка
Установка
Клонировать репозиторий и перейти в каталог проекта:

```shell
git clone https://github.com/fedorov-yu/test_assigment_byuro_1440.git
cd test_assigment_byuro_1440
```
Установить Poetry (https://python-poetry.org/docs/#installation), например:

```shell
pip install poetry
```
Установить зависимости:

```shell
poetry install
```
Активировать виртуальное окружение:

```shell
poetry shell
```
Запуск
Для запуска приложения необходимо предварительно активировать окружение poetry shell, либо запускать через команду poetry run.

Пример запуска для Linux:
```shell
uvicorn src.main:telemetry_driver_app.app  --host 127.0.0.1 --port 8008
```
Тесты
Запуск тестов
```shell
pytest -v tests
```
Есть возможность запускать отдельно End-to-end и Unit тесты:
```shell
pytest -m e2e
pytest -m unit
```
Coverage:
```shell
coverage run -m pytest -m unit && coverage report
```
Линтеры, тайп чекеры
```shell
mypy .
ruff check .
deptry .
```