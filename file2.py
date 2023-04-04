"""Задача №2
Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

get_shop_list_by_dishes(dishes, person_count)
На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
Должен быть следующий результат:

{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
Обратите внимание, что ингредиенты могут повторяться"""

# Импортируем модуль pprint для красивого вывода словарей в консоль
from pprint import pprint

# Объявим функцию get_shop_list_by_dishes(dishes, person_count):
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
    # Создадим внутри функции get_shop_list_by_dishes пустой словарь shop_list для хранения ингредиентов:
    shop_list = {}
    # Далее пройдемся циклом по списку блюд и для каждого блюда получим список ингредиентов.
    # Для этого воспользуемся функцией get_dish(cook_book, dish_name), которую мы создадим далее:
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity']
            # После этого продолжим заполнять словарь shop_list: для каждого ингредиента будем добавлять количество,
            # учитывая количество персон. Если ингредиент уже есть в словаре, будем увеличивать его количество,
            # если нет, то добавим новую запись.
            if name not in shop_list:
                shop_list[name] = {'measure': measure, 'quantity': quantity * person_count}
            else:
                shop_list[name]['quantity'] += quantity * person_count
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))