# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# goods = []
# while input("Вы хотите добавить товар? Введите да или нет: ") == 'да':
#     number = int(input("Введите номер товара: "))
#     features = {}
#     while input("Вы хотите добавить характеристику товара? Введите да или нет: ") == 'да':
#         feature_key = input("Введите номер товара: ")
#         feature_value = input("Введите количество: ")
#         features[feature_key] = feature_value
#     goods.append(tuple([number, features]))
# print(goods)
# #goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
# analitics = {}
# for good in goods:
#     for feature_key, feature_value in good[1].items():
#         if feature_key in analitics:
#             analitics[feature_key].append(feature_value)
#         else:
#          analitics[feature_key] = [feature_value]
# print(analitics)



products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числомю. Попробуйте еще раз.')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue

    unit = tmp

    products.append((
        order,
        {
            'название': title,
            'цена': price,
            'кол-во': amount,
            'ед.изм.': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Формирование списка завершено? (y/n)) ')
    if q.lower() == 'y':
        break

analitics = {
    'название': [],
    'цена': [],
    'кол-во': [],
    'ед.изм.': set()
}

for _, item in products:
    analitics['название'].append(item['название'])
    analitics['цена'].append(item['цена'])
    analitics['кол-во'].append(item['кол-во'])
    analitics['ед.изм.'].add(item['ед.изм.'])

print(analitics)
