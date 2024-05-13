import random
import time


def graph_with_K7(N):
    # создает граф с подграфом K8 и случайными ребрами в оставшейся части графа.

    W = [[0] * N for _ in range(N)]


    # Создать подграф K8
    for i in range(7):
        for j in range(7):
            if i != j:
                W[i][j] = random.randint(1, 100)

    # Добавить случайные ребра в остальную часть графа
    for i in range(7, N):
        for j in range(i+1, N):
            if random.random() < 0.5:
                W[i][j] = random.randint(1, 100)


    return W


start_time = time.time()

N, start, INF = 500, 0, 10 ** 9
# Эти строки устанавливают количество вершин N, начальную вершину start и значение бесконечности INF.

W = []
for i in range(N):
    W.append([])
    for j in range(N):
        if i != j:
            W[i].append(random.randint(0, 10000000))
        else:
            W[i].append(INF)
# создаём граф с N вершинами и случайными весами ребер.

F = [INF] * N
F[start] = 0
# массив F, который будет содержать кратчайшие расстояния от начальной вершины до всех остальных вершин. Расстояние до начальной вершины устанавливается в 0.

number_of_iterations = 0
# для подсчета количества итераций алгоритма.

for k in range(1, N):
    for i in range(N):
        for j in range(N):
            number_of_iterations += 1
            if F[j] + W[j][i] < F[i]:
                F[i] = F[j] + W[j][i]
#алгоритм Флойда-Уоршелла для нахождения кратчайших путей между всеми парами вершин в графе.

print("%s вершин" % N)


for item in F:
    print(item, end=' ')
# массив F, содержащий кратчайшие расстояния до всех вершин.

print(end='\n')
print()

print("Выполнено " + '{:,}'.format(number_of_iterations).replace(',', ' ') + " итераций")

print("%s секунд" % (time.time() - start_time))

