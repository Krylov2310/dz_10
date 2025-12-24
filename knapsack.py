def knapsack(capacity, weights, values):
    """
    Решение задачи о рюкзаке методом динамического программирования.

    Args:
        capacity: вместимость рюкзака
        weights: список весов предметов
        values: список стоимостей предметов

    Returns:
        Максимальная стоимость предметов, которые можно поместить в рюкзак
    """
    n = len(weights)
    weights = sorted(weights)
    # Создаем таблицу DP: (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Заполняем таблицу
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Берем максимум из: (1) не брать предмет, (2) брать предмет
                dp[i][w] = max(
                    dp[i - 1][w],  # не берем предмет
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  # берем предмет
                )
            else:
                dp[i][w] = dp[i - 1][w]  # предмет слишком тяжелый
    return dp[n][capacity]
