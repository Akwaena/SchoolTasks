import itertools

# Изменить формулу и количество аргументов, если потребуется
# Стрелка вверх - and Стрелка вниз - or Палочка - not
f = lambda x, y, z: bool(not z and x or x and y)
# ВАЖНО кортеж из столбцов, а не из строк
table = (
    (0, 0, 0, 0, 1, 1, 1, 1),
    (0, 0, 1, 1, 0, 0, 1, 1),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (0, 1, 0, 1, 0, 0, 0, 1)
)

def recover_table(function, table, arguments):
    for i in itertools.permutations(arguments):
        dictionary = {}
        flag = 0
        for j in range(len(i)): dictionary[i[j]] = table[j]
        for j in range(len(table[0])):
            # Изменить количество аргументов соответственно функции
            if function(dictionary['x'][j], dictionary['y'][j], dictionary['z'][j]) == bool(table[-1][j]):
                flag += 1
        if flag == len(table[-1]):
            return i


print(''.join(recover_table(f, table, 'xyz')))
