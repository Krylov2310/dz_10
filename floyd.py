def floyd_warshall(graph):
    """
    Находит кратчайшие пути между всеми парами вершин в графе.

    Args:
        graph: матрица смежности графа (размер n x n)
               graph[i][j] - вес ребра из i в j
               Если ребра нет, используется float('inf')

    Returns:
        Матрица кратчайших расстояний между всеми парами вершин
    """
    n = len(graph)
    # Создаем матрицу расстояний (копируем исходную)
    dist = [row[:] for row in graph]
    print('=' * 30)
    print('Исходный список:')
    for i in dist:
        print(i)

    print('=' * 30)

    # Основной цикл алгоритма
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Если путь через вершину k короче
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
