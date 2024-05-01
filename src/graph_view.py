from src.graph import Graph


class GraphView:
    @staticmethod
    def display_graph(graph: Graph):
        print("Матрица:")
        print(graph.__str__())
        return

    @staticmethod
    def display_minimal_paths(paths: list[int]):
        print("Минимальная длина пути до каждой вершины:")
        for i in range(len(paths)):
            print(f"Вершина {i}: {paths[i]}")
        return

    @staticmethod
    def display_minimal_tree(minimal_tree: list):
        """
        Вывод минимального остовного дерева.
        """
        print("Рёбра в минимальном остовном дереве:")
        for edge in minimal_tree:
            print(f"{edge[0] + 1} - {edge[1] + 1}")

    @staticmethod
    def display_colors(colors: list[int]):
        if colors is not None:
            print("Раскраска найдена:")
            for i in range(len(colors)):
                print(f"Вершина {i} - Цвет {colors[i]}")
        else:
            print("Раскраска не найдена")
