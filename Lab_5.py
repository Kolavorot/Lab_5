# Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
# сравнительного вычисления данной функции рекурсивно и итерационно. Определить (смоделировать)
# границы применимости рекурсивного и итерационного подхода.
#8 F(n<2) = 1; F(n) = 2F(n-1) + F(n-3) (при n четном), F(n) = 5F(n-1) * F(n-3) (при n нечетном)

# Итерация и рекурсия

import time
import matplotlib.pyplot as mpl

while True:
    n = int(input("Введите натуральное число n >= 0: "))
    if n >= 0:
        break
    else:
        print("Введено неверное число!")

def F_iter(n):
    if n < 2:
        return 1
    f_2 = 1
    f_1 = 1
    f_0 = 1
    f_n = None
    for i in range(2, n + 1):
        if i % 2 == 0:
            f_n = 2 * f_0 + f_2
        else:
            f_n = 5 * f_0 * f_2
        f_2 = f_1
        f_1 = f_0
        f_0 = f_n
    return f_n


def F_rec(n): #Рекурсивное решение
    if n < 2:
        return 1
    elif n >= 2 and n % 2 == 0:
        return 2 * F_rec(n - 1) + F_rec(n - 3)
    elif n >= 2 and n % 2 != 0:
        return 5 * F_rec(n - 1) * F_rec(n - 3)

rec_times = []  # создание списков для построения таблицы значений
rec_values = []
iter_times = []
iter_values = []
n_values = list(range(1, n + 1))

for n in n_values: # заполнение списков
    t0 = time.time()
    iter_values.append(F_iter(n))
    t1 = time.time()
    iter_times.append(t1-t0)
    rec_values.append(F_rec(n))
    t2 = time.time()
    rec_times.append(t2-t1)

table = []  # Таблица значений
for i, n in enumerate(n_values):
    table.append([n, rec_times[i], iter_times[i], rec_values[i], iter_values[i]])
print('{:<4}|{:<25}|{:<25}|{:<25}|{:<25}'.format('n', 'Время рекурсии', 'Время итерации', 'Значение рекурсии', 'Значение итерации'))  # вывод таблицы
print('-' * 105)
for data in table:
    print('{:<4}|{:<25}|{:<25}|{:<25}|{:<25}'.format(data[0], data[1], data[2], data[3], data[4]))

mpl.plot(n_values, iter_times, label='Итерация')
mpl.plot(n_values, rec_times, label='Рекурсия')  # вывод графиков
mpl.xlabel('n')
mpl.ylabel('Время (с)')
mpl.title('Сравнение времени рекурсивного и итерационного подхода')
mpl.legend()
mpl.show()
