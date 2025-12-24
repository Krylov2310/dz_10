from knapsack import *
from lcs import *
from partitions import *
from floyd import *
import os
import platform


def info():
    print(f'\033[33mПрактическое задание 9\n"Алгоритм Дейкстры"\nСтудент Крылов Эдуард Васильевич\n'
          f'Дата: 22.12.2025г.\033[0m\n')


def any_key():
    input('\n\033[33mДля продолжения нажмите "Enter"...\033[0m')


# Очистка консоли
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  # From Linux


# Пример использования
if __name__ == '__main__':
    clear_screen()
    info()
    print_dg = '1. Задача о рюкзаке (0/1 Knapsack)'
    print(f'\033[34m{print_dg}\033[0m')
    print('=' * 55)
    weights = [10, 20, 180, 30, 40]
    values = [60, 100, 120, 220]
    capacity = 150
    print(f'Вместимость рюкзака: {capacity} кг.')
    print(f'Список весов предметов: {weights}')
    print(f'Список стоимостей предметов: {values}')
    print(f'\033[32mВ рюкзак поместится на сумму: \033[0m{knapsack(capacity, weights, values)}')
    print('=' * 55)

    any_key()
    method = '2. Наибольшая общая подпоследовательность (LCS)'
    print(f'\n\033[34m{method}\033[0m')
    str1 = 'ABCBD'
    str2 = 'FBDAC'
    print('=' * 55)
    print(f'Пример 1: {str1} и {str2}')
    lcs_length(str1, str2, vision=True)

    str1 = 'ABCBDAB'
    str2 = 'BDCABA'
    result = lcs_length(str1, str2, vision=True)
    print('=' * 55)
    print(f'Пример 2: {str1} и {str2} = {result}')

    any_key()
    method = '3. Разбиение числа на сумму (число разбиений)'
    print(f'\033[34m{method}\033[0m')
    n = 5
    print('=' * 45)
    print(f'Пример 1: разбиение числа {n}')
    print('=' * 45)
    result = count_partitions(n)
    print(f'\n\033[32mРезультат: \033[0m{result} \033[32mспособа(ов)\033[0m\n')

    print('=' * 45)
    n = 10
    print(f'Пример 2: разбиение числа {n}')
    print('=' * 45)
    result = count_partitions(n)
    print(f'\033[32mРезультат: \033[0m{result} \033[32mспособа(ов)\033[0m')

    any_key()
    method = '4. Алгоритм Флойда-Уоршелла'
    print(f'\n\033[34m{method}\033[0m')
    # Граф с 4 вершинами
    INF = float('inf')
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    result = floyd_warshall(graph)
    print('Результат:')
    for row in result:
        print(row)
    print('=' * 30)

print('\n\033[33mДомашнее задание закончено.\033[0m')
