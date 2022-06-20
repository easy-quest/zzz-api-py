#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from core.core import *


@click.group
def cli():

    with open("report.txt", "wt") as report_file:
        console = Console(file=report_file)
        console.rule(f"Report Generated {datetime.now().ctime()}")

    with console.capture() as capture:
        console.print("[bold red]Hello[/] World")
    str_output = capture.get()


@cli.command
def dialog():
    # text = termux.API.generic('termux-dialog')[1]['text']
    # termux.API.generic('termux-dialo -h')
    # subprocess.Popen(['trans', '-b', '-no-auto', '-no-theme', ':ru'])
    # print(text)
    # print('termux-dialog confirm')
    print(
        Panel.fit(
            'confirm - Show confirmation dialog\n[-i подсказка] текстовая подсказка\n[-t заглавие] задать заголовок диалогового окна'
        ))
    termux.API.generic('termux-dialog confirm -i текстовая -t заглавие')[1]

    # with console.screen():
    # console.print(locals())
    # sleep(5)
    print(
        Panel.fit(
            '\ncheckbox - выберите несколько значений с помощью флажков\n[-v \",,,\"] значения запятой для использования (обязательно)\n[-t title] установить заголовок диалога (необязательно)'
        ))
    text = termux.API.generic('termux-dialog checkbox -t заглавие -v 1,2,3')[1]
    text = termux.API.generic('termux-dialog spinner -v крб,меф,мёд')
    print(text)
    # with console.pager():
    # console.print(make_test_card())

    with console.screen(style="bold white on red") as screen:
        for count in range(5, 0, -1):
            text = Align.center(
                Text.from_markup(f"[blink]Не паникуйте![/blink]\n{count}",
                                 justify="center"),
                vertical="middle",
            )
            screen.update(Panel(text))
            sleep(1)


@click.argument('out',
                type=click.File('a+'),
                default='cmd.json',
                required=False)
@cli.command
def sub_command(out):
    '''Выполнение shell команд с Python.'''
    command_line = Prompt.ask('Введите shell комманду')
    args = shlex.split(command_line)
    args_set = f'subprocess.Popen({args})'
    termux.Clipboard.setclipboard(args_set)
    secho(args_set, file=out)
    if Confirm.ask("Запустить скомпилированную комманду Python?"):
        p = subprocess.Popen(args)  # Success!
    else:
        print("[b]OK :loudly_crying_face:")


@cli.command
def md():
    '''Читает README.md и выводит его содержимое на экрвн'''
    with open("README.md") as readme:
        markdown = Markdown(readme.read())
    console.print(markdown)


@cli.command
@click.argument('out', type=click.File('a+'), default='-', required=False)
@click.option('-r', '--repeat', default=10)
def gps(repeat, out):
    for x, var in enumerate(range(repeat), start=1):
        print(str(x) + ')',
              termux.API.location()[1]['latitude'],
              termux.API.location()[1]['longitude'],
              file=out)


@cli.command
@click.option('-t',
              '--text',
              prompt='Ваш text ru-en',
              default='hello',
              help='Человек, которого нужно поприветствовать.')
@click.argument('out', type=click.File('w'), default='-', required=False)
def trans(text, out):
    #  text = input('ru-en: ')
    t = subprocess.Popen(['trans', ':ru', '-b', '-no-auto', '-p', text])
    ts = subprocess.STDOUT(['trans', ':ru', '-b', '-no-auto', '-p', text])


@cli.command
@click.argument('out',
                type=click.File('a+'),
                default='mydb.json',
                required=False)
def db(out):
    '''Пример простейшей базы данных Python'''
    db = {}
    print(
        'Добро пожаловать в [bold magenta]простейшую базу данных[/bold magenta] :key: "ключ-значение" :vampire:'
    )
    while True:
        print('Что ты хочешь сделать:white_question_mark:')
        # for color in all_colors:
        print(
            "Нажмите [red]P[/red], fg=red),для записи, G для извлечения или L для просмотра содержания"
        )
        print('Для выхода нажмите [bold red blink]Q[/]')
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
