#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def get_shop():

    name = input("Название магазина ")
    product = input("Товар ")
    price = int(input("Цена "))
    return{

        'name': name,
        'product': product,
        'price': price,

    }

def display_shops(shops):

    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 8,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "No",
            "Название.",
            "Товар",
            "Цена"
        )
    )
    print(line)
    for idx, shop in enumerate(shops, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(

                idx,
                shop.get('name', ''),
                shop.get('product', ''),
                shop.get('price', 0)

            )
        )
        print(line)
def select_shops(shops):
    sname = input("Название магазина ")
    cout = 0
    for shop in shops:
        if (shop.get('name') == sname):
            cout = 1
            print(
                ' | {:<5} | {:<5} '.format(
                    shop.get('product', ''),
                    shop.get('price', 0),
                )
            )
        elif cout == 0:
            print("Такого магазина нет")

def main():
    shops = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            shop = get_shop()
            shops.append(shop)
            if len(shops) > 1:
                shops.sort(key=lambda item: item.get('product', ''))

        elif command == 'list':
            display_shops(shops)
        elif command.startswith('select '):
            selected = select_shops(shops)
            display_shops(selected)
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить магазин;")
            print("select - показать товары из заданного магазина;")
            print("list - вывести список магазинов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == '__main__':
    main()
