from random import randint, shuffle
import time
from matplotlib import pyplot as plt
import pylab
import numpy


def generate_test(hardness:int=1):
    """
    Генератор тестов для сортировки
    :param hardness: Коэффицент сложности теста
    :return: Генератор списка теста
    :rtype: generator
    """
    # От hardnessа зависит количество элементов в списке в соотношении 1 к 100
    # И люфт случайности значений оного списка
    for i in range(hardness * 100):
        yield randint(1000 - hardness * 1000, hardness * 1000)


def generate_middle(array:iter, mode:str='average') -> int:
    """
    Генератор среднего значения для алгоритма быстрой сортировки
    Имеет 5 режимов: average - среднее арифметическое, max - максимальное значение, min - минимальное значение,
    random - случайное значение и median - медиана списка
    :param array: Список для выбора метода
    :param mode: Режим работы
    :return: Число-среднее-значение-списка
    :rtype: int
    """
    # Разбиение режимов на случаи, дабы избежать нагромождения if-else конструкций
    cases = {
        'average': lambda x: (max(x) + min(x)) / 2,
        'max': lambda x: max(x),
        'min': lambda x: min(x),
        'random': lambda x: x[randint(0, len(x) - 1)],
        'median': lambda x: numpy.median(x)
    }
    return cases[mode](array)


def quicksort(array:iter, mode:str='average') -> list:
    """
    Функция быстрой сортировки итерируемого объекта, состоящего из чисел
    :param array: Сортируемы итерируемый объект
    :param mode: Режим выбора среднего значения объекта
    :return: Отсортированный список
    :rtype: list
    """
    if len(array) > 1:
        # Случай если список возможно отсортировать
        # Генерация среднего значения
        middle = generate_middle(array, mode)
        # Разбиение значений из оригинального списка на меньшие, равные и большие соответственно относительно среднего значения
        less, equal, greater = list(filter(lambda x: x < middle, array)), list(filter(lambda x: x == middle, array)), list(filter(lambda x: x > middle, array))
        # Конкатенация полученных значений в правильном порядке и передаче их на следующий уровень рекурсии
        return quicksort(less) + equal + quicksort(greater)
    else:
        # Случай если список невозможно отсортировать
        return array


def test_alg(number=10, mode='average', to_print=None):
    """
    Тестер работы алгоритма быстрой сортировки
    :param number: Количество отсортированных для теста списков
    :param mode: Режим выбоа среднего значения сортировки
    :return: Затраченное на сортировку всех списков время в секундах
    :rtype: float
    """
    tests = [list(generate_test(i)) for i in range(number)]
    # Начало отсчета времени выполнения
    start = time.time()
    # Прохождение самих тестов
    for i in range(len(tests)):
        quicksort(tests[i], mode)
    # Окончание отсчета
    time_spent = time.time() - start
    return time_spent


def save(*args, path:str='test', name:str):
    """
    Сохранение времени всех тестов в текстовый файл
    :param args: Списки с данными
    :param name: Имя файла, куда сохранятся результаты
    :return: Списки, записанные в текстовый файл
    """
    with open(f'{path}/{name}.txt', 'w') as file:
        for array in args:
            file.write(str('\n'.join(map(lambda x: str(x), array))).replace('.', ','))
            file.write('\n\t\n')
        file.write(f'Total: {sum([sum(i) for i in args])}')


def load(path:str='test', name:str='test') -> tuple:
    """
    Загрузка времени всех тестов из определенным образом форматированных текстовых файлов
    :param name: Имя папки, откуда надо загрузить результаты
    :return: Кортеж из списков с данными о тестах
    :rtype: tuple
    """
    returned = []
    file = list(filter(lambda x: bool(x), map(lambda x: x.replace('\n', ''), open(f'{path}/{name}.txt', 'r').readlines())))
    temp = []
    for i in file:
        if i != '\t' and i.split(' ')[0] != 'Total:':
            temp.append(float(i))
        else:
            returned.append(temp[:])
            temp.clear()
    return tuple(returned)


def generate_test_results(step=2, test_count=5, save_path='test', save_name='test'):
    """
    Генератор итоговых данных по тестам
    :param step: Шаг сложности тестов
    :param test_count: Количество тестов
    :param save_path: Путь для файла сохранения (без имени самого файла и без слэша в конце)
    :param save_name: Имя файла сохранения (Без расширения)
    :return: Результаты тестов сохраняются в текстовый файл
    """
    print('Начало')
    average_mode = [test_alg(i * step, 'average', to_print=print(f'1 - {i}')) for i in range(test_count + 1)]
    print('avg')
    max_mode = [test_alg(i * step, 'max', to_print=print(f'2 - {i}')) for i in range(test_count + 1)]
    print('max')
    min_mode = [test_alg(i * step, 'min', to_print=print(f'3 - {i}')) for i in range(test_count + 1)]
    print('min')
    random_mode = [test_alg(i * step, 'random', to_print=print(f'4 - {i}')) for i in range(test_count + 1)]
    print('rnd')
    median_mode = [test_alg(i * step, 'median', to_print=print(f'5 - {i}')) for i in range(test_count + 1)]
    print('med')
    print('Готово')

    save(average_mode, max_mode, min_mode, random_mode, median_mode, path=save_path, name=save_name)


def visualize_test_results(save_path='test', save_name='test'):
    """
    Визуализатор предварительно расчитанных данных по времени прохождения тестов
    :param save_path: Путь к файлу сохранения (без имени самого файла и без слэша в конце)
    :param save_name: Имя файла сохранения (Без расширения)
    :return: Визуальный вывод информации
    """
    data = load(save_path, save_name)
    colors = ('red', 'green', 'blue', 'purple', 'black')

    graphic = plt.figure()
    canvas = graphic.add_subplot(1, 1, 1)
    canvas.grid(True, which='both')
    for i in range(len(data)):
        plt.plot(data[i], color=colors[i-1])
    plt.tick_params(axis='both', which='major', labelsize=6)
    canvas.set_xlim(0, 50)
    canvas.set_ylim(0, 15)

    plt.show()


# generate_test_results(4, 50)
# visualize_test_results()
start = time.time()
quicksort(list(generate_test(1000000)), 'average')
time_spent = time.time() - start

print(time_spent)

start = time.time()
quicksort(list(generate_test(1000000)), 'max')
time_spent = time.time() - start

print(time_spent)

start = time.time()
quicksort(list(generate_test(1000000)), 'min')
time_spent = time.time() - start

print(time_spent)

start = time.time()
quicksort(list(generate_test(1000000)), 'random')
time_spent = time.time() - start

print(time_spent)

start = time.time()
quicksort(list(generate_test(1000000)), 'median')
time_spent = time.time() - start

print(time_spent)
