from src.graph_colorer import GraphColorer
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
    num_colors: int = 2
    colorer = GraphColorer(matrix)
    colors = colorer.get_colors(num_colors)
    GraphView.display_colors(colors)
    return


if __name__ == "__main__":
    main()
