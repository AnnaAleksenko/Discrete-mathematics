#include <iostream>
#include <vector>
#include <climits>
#include <Windows.h>
const int INF = INT_MAX; // Значение для недостижимых вершин

void printMatrix(const std::vector<std::vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            if (val == INF) {
                std::cout << "INF ";
            }
            else {
                std::cout << val << " ";
            }
        }
        std::cout << std::endl;
    }
}

void printIncidenceMatrix(const std::vector<std::vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

std::vector<std::vector<int>> adjacencyToIncidence(const std::vector<std::vector<int>>& adjacencyMatrix)
{
    // Получение количества вершин в графе
    int numVertices = adjacencyMatrix.size();
    // Инициализация переменной для подсчета количества рёбер
    int numEdges = 0;

    // Подсчет количества рёбер в графе
    for (int i = 0; i < numVertices; i++) {
        for (int j = i + 1; j < numVertices; j++) {
            // Если между вершинами есть ребро (и оно не равно 0 и не равно INF), увеличиваем счетчик рёбер
            if (adjacencyMatrix[i][j] != 0 && adjacencyMatrix[i][j] != INF) {
                numEdges++;
            }
        }
    }

    // Создание матрицы инцидентности с размером (количество вершин) x (количество рёбер), заполненной нулями
    std::vector<std::vector<int>> incidenceMatrix(numVertices, std::vector<int>(numEdges, 0));
    // Инициализация индекса ребра
    int edgeIndex = 0;

    // Заполнение матрицы инцидентности
    for (int i = 0; i < numVertices; i++) {
        for (int j = i + 1; j < numVertices; j++) {
            // Если между вершинами есть ребро (и оно не равно 0 и не равно INF)
            if (adjacencyMatrix[i][j] != 0 && adjacencyMatrix[i][j] != INF) {
                // Установка соответствующих значений в матрице инцидентности
                incidenceMatrix[i][edgeIndex] = 1; // Вершина i начало ребра
                incidenceMatrix[j][edgeIndex] = -1; // Вершина j конец ребра
                // Увеличение индекса ребра
                edgeIndex++;
            }
        }
    }

    // Возвращаем матрицу инцидентности
    return incidenceMatrix;
}



bool isEulerianGraph(const std::vector<std::vector<int>>& incidenceMatrix)
{ 
    int sum = 0;
    for (const auto& row : incidenceMatrix) {
        for (int val : row) {
            sum += val;
        }
    }
    return sum==0;
}

void floydWarshall(const std::vector<std::vector<int>>& adjacencyMatrix) {
    // Получение количества вершин в графе
    int numVertices = adjacencyMatrix.size();
    // Инициализация матрицы расстояний с размером (количество вершин) x (количество вершин) и заполнение ее значениями INF
    std::vector<std::vector<int>> dist(numVertices, std::vector<int>(numVertices, INF));

    // Копирование значений из матрицы смежности в матрицу расстояний
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            dist[i][j] = adjacencyMatrix[i][j];
        }
    }

    // Алгоритм Флойда-Уоршелла для поиска кратчайших путей между всеми парами вершин
    for (int k = 0; k < numVertices; k++) { // Внешний цикл пробегает по всем вершинам k и используется для промежуточной вершины.
        for (int i = 0; i < numVertices; i++) { // Внутренний цикл пробегает по всем вершинам i и используется для начальной вершины пути.
            for (int j = 0; j < numVertices; j++) { // Еще один внутренний цикл пробегает по всем вершинам j и используется для конечной вершины пути.
                // Проверяем, существует ли более короткий путь из i в j через вершину k.
                if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j]) {
                    // Если существует, обновляем длину кратчайшего пути из i в j.
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }


    // Вывод матрицы смежности
    std::cout << "Матрица смежности:" << std::endl;
    printMatrix(adjacencyMatrix);

    // Вывод матрицы инцидентности
    std::cout << "Матрица инцидентности:" << std::endl;
    printIncidenceMatrix(adjacencyToIncidence(adjacencyMatrix));

    // Вывод матрицы кратчайших путей
    std::cout << "Матрица кратчайших путей:" << std::endl;
    printMatrix(dist);

    // Проверка, является ли граф Эйлеровым
    if (isEulerianGraph(adjacencyToIncidence(adjacencyMatrix))) {
        std::cout << "Граф является Эйлеровым" << std::endl;
    }
    else {
        std::cout << "Граф не является Эйлеровым" << std::endl;
    }
}


int main() {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    // Пример матрицы смежности
    std::vector<std::vector<int>> adjacencyMatrix = {
        {0, 15, INF, INF, INF, 16, INF, INF},
        {INF, 0, INF, 16, INF, 11, 13, INF},
        {INF, INF, 0, INF, INF, INF, INF, INF},
        {INF, INF, 15, 0, 11, 18, 13, INF},
        {INF, INF, INF, INF, 0, 13, INF, INF},
        {INF, 19, 13, INF, INF, 0, 14, INF},
        {INF, INF, 16, INF, INF, INF, 0, 19},
        {16, INF, INF, 18, INF, 17, INF, 0}
        
    };

    // Выводим информацию
    floydWarshall(adjacencyMatrix);

    return 0;
}