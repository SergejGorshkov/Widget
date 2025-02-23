# Виджет финансовых операций клиента

Проект написан на Python, в нем реализуются функции маскировки номеров банковских карт и счетов, а также предоставляет 
возможность фильтрации данных о финансовых операциях клиента по различным параметрам.

## Структура проекта

Проект состоит из следующих модулей:

1. masks.py. 
   Содержит функции для маскировки номеров банковской карты и счета. 
   Возвращает замаскированные номера карты и счета.
   
2. widget.py:
   Содержит функцию, которая принимает данные с типом и номером банковской карты или счета, 
   и возвращает маску номера карты или счета. Использует разные типы маскировки для карт и счетов.

3. processing.py:
   Содержит функции, которые принимает данные о финансовых операциях клиента и, опционально, параметры для их 
   фильтрации по дате и статусу исполнения.
   Возвращает отфильтрованные по заданным значениям данные.
  
## Проверка кода

В проекте выполнены проверки линтерами:
- Flake8: для проверки стиля кода;
- mypy: для статической типизации;
- black: для автоматического форматирования кода;
- isort: для сортировки импортов.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/SergejGorshkov/Widget.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Так как проект еще находится в разработке, в тестовом режиме пока что можно работать в PyCharm с отдельными модулями:
- в модуле masks.py можно в интерактивном режиме ввести свои номера банковской карты и счета и получить в терминале 
  их маски;
- в модуле widget.py можно получить маски карты или счета, а также дату в формате "ДД.ММ.ГГГГ", используя 
  файлы for_testing_masks.txt и for_testing_date.txt (их можно дополнять своими значениями).
- в модуле processing.py можно получить отфильтрованные по заданным значениям данные, добавив в конец файла 
  код следующего вида:

*для сортировки банковских операций по статусу исполнения:*
```
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
"CANCELED"))
```
*для сортировки банковских операций по дате выполнения операции:*
```
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
"False"))
```
  