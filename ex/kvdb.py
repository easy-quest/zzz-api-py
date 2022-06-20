#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-
from core.core import *

db = {}


@click.argument('out',
                type=click.File('w'),
                default='mydb.json',
                required=False)
def cli(out):
    '''Пример простейшей базы данных Python'''
    print(
        'Добро пожаловать в [bold magenta]простейшую базу данных[/bold magenta] :key: "ключ-значение" :vampire:'
    )
    while True:
        print('Что ты хочешь сделать:white_question_mark:')
        print(
            'Нажмите P для записи, G чтобы извлечения или L для просмотра  содержания'
        )
        print('Для выхода нажмите Q')
        action = click.getchar()
        if action == 'P' or action == 'p':
            k = input('Введите ключ: ')
            d = input('Введите значение: ')
            db[k] = d
        elif action == 'G' or action == 'g':
            k = input('Введите ключ: ')
            if not k in db:
                print('Нет такого ключа')
            else:
                print('Ваши данные: %s' % db[k])
        elif action == 'L' or action == 'l':
            print('DB содержание:')
            print(db)
        elif action == 'Q' or action == 'q':
            print('До встречи!!!')
            print(db, file=out)
            break
