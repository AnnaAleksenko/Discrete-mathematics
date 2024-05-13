#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstdlib>
#include <ctime>
#include <Windows.h>
using namespace std;

// Структура, представляющая ребро в графе
struct Edge {
	int from, to, capacity, flow;
};

class FordFulkerson {
private:
	int n;
	vector<vector<int>> graph;
	vector<Edge> edges;
	vector<bool> visited;

	// Поиск увеличивающего пути в графе с использованием DFS
	int dfs(int node, int min_capacity, int t) {
		if (node == t) // Если достигнут сток, возвращаем минимальную пропускную способность на пути
			return min_capacity;

		visited[node] = true;
		for (int i = 0; i < n; ++i) {
			if (!visited[i] && graph[node][i] > 0) {
				int new_min_capacity = min(min_capacity, graph[node][i]);
				int flow = dfs(i, new_min_capacity, t);
				if (flow > 0) {
					// Обновляем пропускные способности рёбер
					graph[node][i] -= flow;
					graph[i][node] += flow;
					return flow;
				}
			}
		}
		return 0;
	}

	// Поиск всех вершин, достижимых из источника после насыщения потока
	void bfs(int s, vector<bool>& reachable) {
		fill(reachable.begin(), reachable.end(), false);
		queue<int> q;
		q.push(s);
		reachable[s] = true;
		while (!q.empty()) {
			int node = q.front();
			q.pop();
			for (int i = 0; i < n; ++i) {
				if (!reachable[i] && graph[node][i] > 0) {
					reachable[i] = true;
					q.push(i);
				}
			}
		}
	}

public:
	FordFulkerson(int num_nodes) : n(num_nodes) {
		graph.assign(n, vector<int>(n, 0));
		visited.assign(n, false);
	}

	// Добавление ребра в граф
	void addEdge(int from, int to, int capacity) {
		Edge e1 = { from, to, capacity, 0 };
		Edge e2 = { to, from, 0, 0 }; // Обратное ребро для обратного потока
		graph[from][to] = capacity;
		graph[to][from] = 0;
		edges.push_back(e1);
		edges.push_back(e2);
	}

	// Поиск максимального потока методом Форда-Фалкерсона
	int findMaxFlow(int s, int t) {
		int max_flow = 0;
		while (true) {
			fill(visited.begin(), visited.end(), false);
			int flow = dfs(s, INT_MAX, t); // Ищем увеличивающий путь
			if (flow == 0) break; // Если увеличивающий путь не найден, завершаем поиск
			max_flow += flow; // Добавляем найденный поток к общему потоку
		}
		return max_flow;
	}

	// Нахождение разреза после нахождения максимального потока
	void findMinCut(int s, int t) {
		vector<bool> reachable(n, false);
		bfs(s, reachable);
		cout << "Разрез (вершины, достижимые из источника S): ";
		for (int i = 0; i < n; ++i) {
			if (reachable[i]) {
				cout << i << " ";
			}
		}
		cout << endl;
	}

	// Вывод всех рёбер графа с их пропускными способностями
	void printEdges() {
		cout << "Сгенерированные рёбра графа:" << endl;
		for (const auto& edge : edges) {
			cout << edge.from << " -> " << edge.to << ", пропускная способность: " << edge.capacity << endl;
		}
	}
};

int main() {
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	srand(time(0)); // Инициализация генератора случайных чисел

		// Создание графа и добавление рёбер с случайными пропускными способностями
		FordFulkerson graph(10); // Ваш граф содержит 10 вершин
	graph.addEdge(0, 1, rand() % 901 + 100); // из A в C с случайной пропускной способностью от 100 до 1000
	graph.addEdge(0, 2, rand() % 901 + 100); // из S в C с случайной пропускной способностью от 100 до 1000
	graph.addEdge(0, 3, rand() % 901 + 100); // из S в A с случайной пропускной способностью от 100 до 1000
	graph.addEdge(1, 2, rand() % 901 + 100); // из S в D с случайной пропускной способностью от 100 до 1000
	graph.addEdge(1, 5, rand() % 901 + 100); // из S в B с случайной пропускной способностью от 100 до 1000
	graph.addEdge(3, 2, rand() % 901 + 100); // из B в D с случайной пропускной способностью от 100 до 1000
	graph.addEdge(3, 4, rand() % 901 + 100); // из C в E с случайной пропускной способностью от 100 до 1000
	graph.addEdge(4, 2, rand() % 901 + 100); // из C в F с случайной пропускной способностью от 100 до 1000
	graph.addEdge(4, 7, rand() % 901 + 100); // из D в E с случайной пропускной способностью от 100 до 1000
	graph.addEdge(5, 2, rand() % 901 + 100); // из D в F с случайной пропускной способностью от 100 до 1000
	graph.addEdge(5, 6, rand() % 901 + 100); // из E в G с случайной пропускной способностью от 100 до 1000
	graph.addEdge(5, 8, rand() % 901 + 100); // из E в H с случайной пропускной способностью от 100 до 1000
	graph.addEdge(7, 2, rand() % 901 + 100); // из F в G с случайной пропускной способностью от 100 до 1000
	graph.addEdge(7, 6, rand() % 901 + 100); // из F в H с случайной пропускной способностью от 100 до 1000
	graph.addEdge(7, 9, rand() % 901 + 100); // из G в H с случайной пропускной способностью от 100 до 1000
	graph.addEdge(7, 10, rand() % 901 + 100); // из G в T с случайной пропускной способностью от 100 до 1000
	graph.addEdge(2, 6, rand() % 901 + 100); // из H в T с случайной пропускной способностью от 100 до 1000
	graph.addEdge(8, 6, rand() % 901 + 100);
	graph.addEdge(8, 10, rand() % 901 + 100);
	graph.addEdge(9, 10, rand() % 901 + 100);

	// Вывод всех рёбер графа
	graph.printEdges();

	// Нахождение максимального потока в графе
	int max_flow = graph.findMaxFlow(0, 9); // S - вершина 0, T - вершина 9
	cout << "\nМаксимальный поток: " << max_flow << endl;

	// Нахождение минимального разреза
	graph.findMinCut(0, 9); // S - вершина 0, T - вершина 9

	return 0;
}