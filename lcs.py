def lcs_length(str1, str2, vision=False):
    """
    Находит длину наибольшей общей подпоследовательности (LCS) двух строк.
    При verbose=True выводит пошаговое заполнение таблицы DP и итоговый отчёт.


    Args:
        str1 (str): первая строка
        str2 (str): вторая строка
        vision (bool): если True — выводит детализацию процесса

    Returns:
        int: длина LCS
    """
    m, n = len(str1), len(str2)

    # Создаем таблицу DP (m+1) x (n+1), инициализируем нулями
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    if vision:
        print("=" * 55)
        # print('АЛГОРИТМ LCS: НАИБОЛЬШАЯ ОБЩАЯ ПОДПОСЛЕДОВАТЕЛЬНОСТЬ')

        print(f'Строка 1: "{str1}" (длина = {m})')
        print(f'Строка 2: "{str2}" (длина = {n})')
        print(f'\nСоздана таблица DP размером {m + 1}×{n + 1} (с нулевыми границами)')
        # print('=' * 55)

    # Заполняем таблицу DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Символы совпадают — берём диагональ + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Символы не совпадают — берём максимум из верхней/левой ячейки
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    result = dp[m][n]

    if vision:

        print(f'Длина LCS = {result}')
        print('=' * 55)
        if result > 0:
            lcs = reconstruct_lcs(dp, str1, str2)
            print(f'Одна из возможных LCS: "{lcs}"')
        else:
            print('=' * 55)
            print('LCS не найдена (общих символов нет)')
        print('\nФинальная таблица DP:')
        print_dp_table(dp, str1, str2)
        print('=' * 55)
    return result


def print_dp_table(dp, str1, str2):
    # Вспомогательная функция: выводит таблицу DP с заголовками
    m, n = len(dp), len(dp[0])
    # Формируем заголовки столбцов
    col_header = f'   " ' + ' '.join(f'{c:>2}' for c in str2)
    print(f'\033[32m{col_header}\033[0m')
    # Печатаем строки
    for i in range(m):
        if i == 0:
            row_label = '"'
        else:
            row_label = str1[i - 1]
        row = f'\033[35m{row_label}\033[0m ' + ' '.join(f'{dp[i][j]: > 2}' for j in range(n))
        print(f'{row}')


def reconstruct_lcs(dp, str1, str2):
    # Восстанавливает одну из возможных LCS по заполненной таблице DP
    i, j = len(str1), len(str2)
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs))
