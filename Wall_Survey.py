turn_number, turns = input(), input()


def find_wall(turns: str, vehicle_coord: tuple = (0, 0)) -> tuple:
    """
    Обнаруживает стену по последовательности ходов марсохода
    :param turns: строка из плюсов и минусов, характеризующая перемещение марсохода
    :param vehicle_coord: кортеж из начальных XY координат марсохода
    :return: Y координата стены
    :rtype: Tuple
    """
    coord = list(vehicle_coord)
    history = [coord[1]]
    for i in turns:
        if i == '+':
            coord[1] += 1
        elif i == '-':
            coord[1] -= 1
        coord[0] += 1
        history.append(coord[1])
    return max(history), history


wall = find_wall(turns)
print(len(list(filter(lambda x: x == wall[0], wall[1]))))
