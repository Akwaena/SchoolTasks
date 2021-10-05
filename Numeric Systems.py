from functools import reduce


def generate_digits(base) -> list:
    """
    Генератор массива цифр для base-ичной системы счисления
    :param int base: база для системы счисления для которой нужны цифры
    :return:
    :rtype: list
    """
    return [i for i in range(base)]


def convert_to_decimal(number, base) -> int:
    """
    Конвертор числа из base-ичной системы в десятичную
    У стандартного int base <= 36, а у меня base любое
    :param str number: число в base-ичной системе счисления, цифры писать через пробел
    :param int base: база числа number
    :return: Число в десятичной системе счисления, пробелов между числами нет
    :rtype: int
    """
    returned = 0
    num = number.split()
    for i in range(len(num)):
        returned += int(num[i]) * (base ** (len(num) - i - 1))
    return returned


def reverse_str(string) -> str:
    returned = ''
    for i in reversed(string.split()):
        returned += '{} '.format(i)
    return returned


def convert_from_decimal(number, base) -> str:
    """
    Конвертор числа из десятичной в base-ичную
    :param number: число в десятичной системе счисления
    :param base: база требуемого числа
    :return: Число в base-ичной системе счисления, цифры записаны через пробел
    :rtype: str
    """
    digits = generate_digits(base)
    returned = ''
    n = [number][0]

    while n:
        n, x = divmod(int(n), base)
        returned += '{} '.format(digits[x])
    return ''.join(reverse_str(returned))


def main():
    while True:
        command = input('Введите команду: ').split('=')
        if command[0] in ('помощь', 'справка', 'команды'):
            print('помощь/справка/команды - получить список команд и справку о программе')
            print('конвертировать/перевести={число}={база_н}={база_к} - перевести число из базы н в базу к')
            print('выход/выйти - выйти из программы')
        elif command[0] in ('конвертировать', 'перевести'):
            print('Результат выполнения команды: ', convert_from_decimal(convert_to_decimal(command[1],
                                                                                            int(command[2])),
                                                                         int(command[3])))
        elif command[0] in ('выход', 'выйти'):
            exit(0)


main()
