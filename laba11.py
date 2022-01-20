#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def main():
    trains = []
    while True:
        command = get_command()
        if command == 'exit':
            break

        elif command == 'add':
            trains.append(add())
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('time', ''))

        elif command == 'list':
            print_list(trains)

        elif command.startswith('select '):
            select(command, trains)

        elif command == 'help':
            print_help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


def get_command():
    return input(">>> ").lower()


def add():
    dist = input("Название пункта назначения? ")
    num = int(input("Номер поезда? "))
    time = input("Время отправления ЧЧ:ММ? ")
    time = datetime.strptime(time, '%H:%M')
    train = {
        'dist': dist,
        'num': num,
        'time': time,
    }
    return train


def print_list(trains):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 28,
        '-' * 14,
        '-' * 19
    )
    print(line)
    print(
        '| {:^4} | {:^28} | {:^14} | {:^19} |'.format(
            "No",
            "Название пункта назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)
    for idx, train in enumerate(trains, 1):
        print(
            '| {:>4} | {:<28} | {:<14} | {:>19} |'.format(
                idx,
                train.get('dist', ''),
                train.get('num', ''),
                train.get('time', 0).strftime("%H:%M")
            )
        )
    print(line)


def print_help():
    print("Список команд:\n")
    print("add - добавить отправление;")
    print("list - вывести список отправлений;")
    print("select <ЧЧ:ММ> - вывод на экран информации о "
          "поездах, отправляющихся после этого времени;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def select(command, trains):
    count = 0
    parts = command.split(' ', maxsplit=1)
    dist = parts[1]
    for train in trains:
        if train.get("dist").lower() == dist:
            count += 1
            if count == 1:
                line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                    '-' * 4,
                    '-' * 28,
                    '-' * 14,
                    '-' * 19
                )
                print(line)
                print(
                    '| {:^4} | {:^28} | {:^14} | {:^19} |'.format(
                        "No",
                        "Название пункта назначения",
                        "Номер поезда",
                        "Время отправления"
                    )
                )
                print(line)
            print(
                '| {:>4} | {:<28} | {:<14} | {:>19} |'.format(
                    count,
                    train.get('dist', ''),
                    train.get('num', ''),
                    train.get('time', 0).strftime("%H:%M")
                )
            )
    if count == 0:
        print("Отправлений в такой город нет.")
    else:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 28,
            '-' * 14,
            '-' * 19
        )
        print(line)


if __name__ == '__main__':
    main()
