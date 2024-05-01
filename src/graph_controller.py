from src.graph import Graph
from src.graph_methods import GraphMethods


class GraphController:
    @staticmethod
    def input_graph() -> Graph:
        n = int(input("Введите количество вершин в графе: "))
        graph = []
        for _ in range(n):
            row = list(map(int, input().split()))
            graph.append(row)
        return Graph(graph)

    @staticmethod
    def input_matrix_adjacency() -> list[list[int]]:
        n = int(input("Введите количество вершин в графе: "))
        print("Введите матрицу смежности построчно (веса ребер через пробел, 0 - если нет ребра):")
        graph = []
        for _ in range(n):
            row = list(map(int, input().split()))
            graph.append(row)
        return graph

    @staticmethod
    def find_min_paths(graph: Graph) -> list[int]:
        return GraphMethods.find_min_paths(graph.get_matrix())
