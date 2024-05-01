from src.graph import Graph
from src.graph_view import GraphView


def main():
    matrix = [
        [0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0]
    ]

    graph: Graph = Graph(matrix)
    minimal_tree: list = graph.get_minimal_tree_by_prim_algorithm()
    GraphView.display_minimal_tree(minimal_tree)
    return


if __name__ == "__main__":
    main()
