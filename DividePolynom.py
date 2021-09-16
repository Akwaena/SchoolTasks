from sympy import *
from random import randint


def generate_polynom(deg_num, coeff=(-9, 9)):
    print('Генерируем многочлен')
    returned = ''

    for i in range(deg_num + 1):
        if deg_num - i > 1:
            returned += f'{randint(int(coeff[0]), int(coeff[1]))} * (x ** {deg_num - i}) + '
        elif deg_num - i == 1:
            returned += f'{randint(int(coeff[0]), int(coeff[1]))} * x + '
        else:
            returned += str(randint(int(coeff[0]), int(coeff[1])))

    return returned


def divide_polynom(pol_1, pol_2, mode='all'):
    print('Делим многочлен')
    if mode == 'all':
        return div(pol_1, pol_2, domain='QQ')
    elif mode == 'int':
        return div(pol_1, pol_2, domain='QQ')[0]
    elif mode == 'rest':
        return div(pol_1, pol_2, domain='QQ')[1]


def check_human(test_num, auto=False):
    print('Начат тест')
    succ = 0
    for i in range(test_num):
        divided = generate_polynom(5)
        divider = generate_polynom(2)
        if not auto:
            answer = input(f'Найдите остаток: ({divided}) / ({divider}): ')
        else:
            print(f'Найдите остаток: ({divided}) / ({divider})')
            answer = divide_polynom(divided, divider, mode='rest')
        if answer == divide_polynom(divided, divider, mode='rest'):
            print('Правильно!')
            succ += 1
        else:
            print('Не правильно!')

    print(f'Вы правильно решили {succ}/{test_num}')


def main():
    print('Добро пожаловать в тест на деления многочленов')
    print('Для получения списка команд введите help')
    while True:
        command = input('Введите команду: ')

        if command == 'help':
            print('Список команд: ')
            print('exit или quit - выход из программы')
            print('help - получить список комманд')
            print('start test - начать тест')
            print('auto test - начать тест, который решится автоматически')
            print('generate - сгенерировать многочлен')
            print('divide - поделить два многочлена')
        elif command == 'exit' or command == 'quit':
            print('Выход из программы...')
            quit(0)
        elif command == 'start test':
            check_human(int(input('Введите количество заданий: ')), auto=False)
        elif command == 'generate':
            deg_num = int(input('Введите максимальную степень: '))
            print('Если хотите оставить стандартный разброс коэффицента - не вводите ничего')
            coeff = (input('Введите наименьшее значение коэффицента: '), input('Введите наибольшее значение '
                                                                               'коэффицента: '))

            if coeff[0] != '' or coeff[1] != '':
                print(generate_polynom(deg_num, coeff))
            else:
                print(generate_polynom(deg_num))
        elif command == 'auto test':
            check_human(int(input('Введите количество заданий: ')), auto=True)
        else:
            print('Команды не существует')
        print()


main()
