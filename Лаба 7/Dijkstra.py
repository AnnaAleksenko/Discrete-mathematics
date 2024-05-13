import random
import time

def graph_with_K7(N):
    a = [[0] * N for _ in range(N)]

    # Создать подграф K7
    for i in range(7):
        for j in range(7):
            if i != j:
                a[i][j] = random.randint(1, 100)

    # Добавить случайные ребра в остальную часть графа
    for i in range(7, N):
        for j in range(i+1, N):
            if random.random() < 0.4:
                a[i][j] = random.randint(1, 100)

    return a

# Функция Дейкстры для поиска кратчайших путей в графе
def Dijkstra(N, S, matrix):
    # Количество итераций
    number_of_iterations = 0

    # Массив посещенных вершин
    valid = [True] * N

    # Массив весов
    weight = [1000000] * N

    # Устанавливаем вес начальной вершины в 0
    weight[S] = 0

    # Проходим по всем вершинам
    for k in range(N):
        # Находим вершину с минимальным весом
        min_weight = 1000001
        ID_min_weight = -1
        for k in range(N):
            if valid[k] and weight[k] < min_weight:
                min_weight = weight[k]
                ID_min_weight = k

        # Обновляем веса для всех смежных вершин
        for z in range(N):
            number_of_iterations += 1
            if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
                weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]

        # Помечаем найденную вершину как посещенную
        valid[ID_min_weight] = False

    # Выводим количество итераций
    print('{:,}'.format(number_of_iterations).replace(',', ' ') + " итераций")

    # Возвращаем массив весов
    return weight

# Замеряем время выполнения алгоритма
start_time = time.time()

# Считываем количество вершин
n = int(input("Введите количество вершин:"))

# Создаем матрицу смежности
m = n
a = [[0] * m] * n
for i in range(len(a)):
    for j in range(len(a[i])):
        if i != j:
            # Генерируем случайный вес ребра
            a[i][j] = random.randint(1, 500)
        else:
            # Вес ребра из вершины в саму себя равен бесконечности
            a[i][j] = 1000000

# Выполняем алгоритм Дейкстры
ans = Dijkstra(n, 0, a)

# Выводим результаты
print("Количество вершин: " + str(n))
print(ans)
print(f"{(time.time() - start_time)} секунд")
