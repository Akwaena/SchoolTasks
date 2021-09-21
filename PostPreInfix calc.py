from trans_from_infix import *

operators = {
    '+': (lambda x, y: x + y, 2),
    '-': (lambda x, y: x - y, 2),
    '*': (lambda x, y: x * y, 1),
    '/': (lambda x, y: y // x, 1)
}


def input_check(input_expression):
    if not input_expression:
        print('Выражение пусто')
        return False

    if len(input_expression.split()) < 3:
        print('Выражение содержит недостаточно элементов')
        return False

    for i in input_expression:
        if i not in operators.keys() and not i.isdigit() and not ' ':
            print('Выражение содержит некорректный символ "{}"'.format(i))
            return False

    #    temp = [0, 0]
    #    for i in input_expression:
    #        if i.isdigit():
    #            temp[0] += 1
    #        elif i in operators.keys():
    #            temp[1] += 1
    #    if temp[0] / 2 != temp[1]:
    #        raise Exception('Недостаточно операторов')

    print('Проверка корректности выражения пройдена')
    return True


def exp_type(expression):
    print('Вычисляем тип выражения')
    if input_check(expression):
        if expression[0] in operators.keys():
            return 'prefix_type'
        elif expression[-1] in operators.keys():
            return 'postfix_type'
        else:
            return 'infix_type'


def calculate_exp(input_expression):
    print('Расчет выражения')

    if input_expression[0] in operators.keys():
        returned = pre_to_inf(input_expression)
    elif input_expression[-1] in operators.keys():
        returned = post_to_inf(input_expression)
    else:
        returned = input_expression
    print('Расчет {}'.format(returned))
    return eval(returned)


def post_to_inf(post_exp):
    print('Конвертация Постфикс в Инфикс  {}'.format(post_exp))
    expression, stack = post_exp.split(), list()

    for i in expression:
        if i.isdigit():
            stack.append(i)
        elif i in operators.keys():
            stack.append('({} {} {})'.format(stack.pop(-2), i, stack.pop()))

    return stack[-1]


def pre_to_inf(pre_exp):
    print('Конвертация Префикс в Инфикс  {}'.format(pre_exp))
    expression = pre_exp.split()
    while len(expression) != 1:
        pose_op = 0
        for num in range(len(expression)):
            if expression[num] in operators.keys():
                pose_op = num
        part = '( ' + str(expression[pose_op + 1]), str(expression[pose_op]), str(expression[pose_op + 2]) + ' )'
        expression[pose_op + 2] = part
        del expression[pose_op:pose_op + 2]
    return str(expression[0]).replace(',', '').replace('"', '').replace("'", '').replace('((', '(') \
               .replace('))', ')')[1:-1]


def inf_to_post(inf_exp):
    print('Переводим инфикс в постфикс | {}'.format(inf_exp))
    return trans_from_infix(inf_exp, 'postfix')[0]


def inf_to_pre(inf_exp):
    print('Переводим инфикс в префикс | {}'.format(inf_exp))
    return trans_from_infix(inf_exp, 'prefix')[0]


def convert(expression, to_type):
    print('Конвертируем {} в {}'.format(expression, to_type))
    if input_check(expression):
        if exp_type(expression) == 'infix_type':
            if to_type == 'префикс':
                inf_to_pre(expression)
            elif to_type == 'постфикс':
                inf_to_post(expression)
            else:
                return expression
        elif exp_type(expression) == 'prefix_type':
            if to_type == 'инфикс':
                return pre_to_inf(expression)
            elif to_type == 'постфикс':
                return inf_to_post(pre_to_inf(expression))
            else:
                return expression
        elif exp_type(expression) == 'postfix_type':
            if to_type == 'инфикс':
                return post_to_inf(expression)
            elif to_type == 'префикс':
                return inf_to_pre(post_to_inf(expression))
            else:
                return expression


def args_check(commands, args):
    print('Проверяем введенную команду')
    if len(commands) != args:
        print('Недостаточно аргументов к команде')
        return False
    else:
        return True


def main():
    print('Калькулятор и преобразователь Инф/Пост/Префиксных выражений')
    print('Для получения списка команд введите "помощь", "справка" или "команды"')
    while True:
        commands = input('Введите команду: ').split(' / ')

        if commands[0].lower() in ('выйти', 'выход'):
            print('Выход...')
            exit(0)
        elif commands[0].lower() in ('вычислить', 'посчитать'):
            print('Определена команда на расчет выражения')
            if args_check(commands, 2):
                if input_check(commands[1]):
                    print('Ответ: ', calculate_exp(commands[1]))
        elif commands[0].lower() in ('определить', 'определить тип'):
            print('Определена команда на определение типа выражения')
            if args_check(commands, 2):
                if exp_type(commands[1]) == 'infix_type':
                    print('Выражение записано в инфиксной нотации')
                elif exp_type(commands[1]) == 'prefix_type':
                    print('Выражение записано в префиксной нотации')
                elif exp_type(commands[1]) == 'postfix_type':
                    print('Выражение записано в постфиксной нотации')
        elif commands[0] in ('перевести', 'конвертировать'):
            print('Определена команда на конвертацию выражения')
            if args_check(commands, 2):
                print('Ответ: {}'.format(convert(commands[1].split(" в ")[0], commands[1].split(" в ")[1])))
        elif commands[0].lower() in ('помощь', 'команды', 'справка'):
            print('помощь/команды/справка -- получить список команд и справку')
            print('выход/выйти -- покинуть программу')
            print('определить/определить тип /{выражение} -- определяет нотацию выражения')
            print('вычислить/посчитать / {выражение} -- вычисляет заданное выражение')
            print('перевести/конвертировать / {выражение} в {тип} -- переводит выражение в заданный тип (инфикс, '
                  'постфикс, префикс)\n')
            print('Оператор математических выражений различных нотаций')
            print('Функционал включает в себя: конвертацию выражений в другие нотации, вычисление выражений различной '
                  'нотации, определение нотации выражения\n')
            print('Версия 1.3')
            print('Разработчик -- Akwaena')
            print('По заказу Зелениной С.Б.')
            print('Сентябрь 2021')

        print()


main()
