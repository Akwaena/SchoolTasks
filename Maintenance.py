def check_part(part: int, mileage: int) -> bool:
    """
    :param mileage: Пробег машины
    :param part: Срок службы детали
    :return: Заменялась ли деталь на прошлом ТО
    :rtype: bool
    """
    if mileage - (mileage // part) * part <= 15000:
        return True
    return False


def check_parts(parts: list, mileage: int) -> None:
    """
    :param parts: Список списков из названия детали и периода ТО
    :param mileage: Пробег машины
    :return: Выводит в консоль число замененных запчастей и их названия
    """
    returned = list(filter(lambda x: check_part(int(x[1]), mileage), parts))
    returned.sort()
    print(len(returned))
    for i in returned:
        print(i[0])


parts_number, mileage = input().split()
parts_number, mileage = int(parts_number), int(mileage)
parts = [input().split() for i in range(parts_number)]
check_parts(parts, mileage)
