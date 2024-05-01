from src.graph import Graph
from src.graph_controller import GraphController
from src.graph_view import GraphView


def main():
    matrix = [
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1]
    ]

    graph: Graph = Graph(matrix)
    paths: list[int] = GraphController.find_min_paths(graph)
    GraphView.display_minimal_paths(paths)
    return


if __name__ == "__main__":
    main()
