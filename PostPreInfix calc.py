operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: y // x
}


def input_check(input_expression):
    if not input_expression:
        print('Выражение пусто (Err1)')
        exit(0)

    if len(input_expression.split()) < 3:
        print('Выражение некорректно (Err2)')
        exit(0)

    for i in input_expression:
        if i not in operators.keys() and not i.isdigit() and not ' ':
            print(f'Выражение содержит некорректный символ "{i}" (Err3)')
            exit(0)

    temp = [0, 0]
    for i in input_expression:
        if i.isdigit():
            temp[0] += 1
        elif i in operators.keys():
            temp[1] += 1
    if temp[0] / 2 != temp[1]:
        print('Выражение некорректно (Err4)')
        exit(0)

    print('Проверка корректности выражения пройдена')


def calculate_infix_exp(input_expression):
    print('Расчет инфиксного выражения')
    print(int(eval(input_expression)))


def calculate_postfix_exp(input_expression):
    print('Расчет постфиксного выражения')
    returned = list()
    for char in input_expression.split():
        if char.isdigit():
            returned.append(int(char))
        else:
            returned.append(operators[char](returned.pop(), returned.pop()))

    print(returned[0])


def calculate_prefix_exp(input_expression):
    print('Расчет богомерзкого префиксного выражения')
    pass


def main():
    input_expression = input('Введите выражение: ')
    input_check(input_expression)
    if input_expression[0] in operators.keys():
        calculate_prefix_exp(input_expression)
    elif input_expression[-1] in operators.keys():
        calculate_postfix_exp(input_expression)
    else:
        calculate_infix_exp(input_expression)

    print()


print('Калькулятор Инф/Пост/Префиксных выражений')

while True:
    main()
