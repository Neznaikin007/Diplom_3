## Дипломный проект. Задание 3: UI-тесты
<hr>

## Студент: Роман Попов

## <h>Когорта: #28+29_qa_FS</h>
<hr>

## <h>Project: Stellar Burgers</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest --alluredir=allure_results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла           | Содержание файла                   |
|--------------------------|------------------------------------|
| Tests dir                | Директория с тестами               |
| test_check_base_funct.py | Тесты на основную функциональность |
| test_order_feed.py       | Тесты на создание заказа           |
| conftest.py              | Фикстуры                           |
| helpers.py               | Хэлпер для тела запросов           |
| data.py                  | Файл с body запросов               |
| curls.py                 | Файл с URL                         |
| requirements.txt         | Файл с зависимостями               |
| allure_results.dir       | Папка с отчетами Allure            |

