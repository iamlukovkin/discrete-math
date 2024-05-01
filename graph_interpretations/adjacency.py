from graph_interpretations.graph import Graph
from graph_interpretations.line import Line


class Adjacency:
    __matrix: list
    __graph: Graph

    def __init__(self, matrix=None, graph=None):
        if matrix is not None:
            self.__graph = Graph()
            if len(matrix) != len(matrix[0]):
                raise ValueError("Matrix must be square")
            self.set_matrix(matrix)
        elif graph is not None:
            self.__graph = graph
            self.set_matrix()

    def get_graph(self):
        if self.__graph.get_lines_count() == 0:
            self.set_graph()
        return self.__graph

    def get_matrix(self):
        return self.__matrix

    def set_matrix(self, matrix=None):
        if matrix is not None:
            self.__matrix = matrix
        else:
            self.create_zero_matrix()
            for i in range(self.__graph.get_lines_count()):
                line = self.__graph.get_lines()[i]
                self.__matrix[line.get_source()][line.get_target()] = 1

    def create_zero_matrix(self):
        self.__matrix = [[0 for _ in range(self.__graph.get_points_count())]
                         for _ in range(self.__graph.get_points_count())]

    def set_graph(self, graph: Graph = None):
        if graph is None:
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix)):
                    if self.__matrix[i][j] == 1:
                        self.__graph.add_line(Line(i, j))
        else:
            self.__graph = graph

    def __str__(self):
        result = "Adjacency matrix: \n"
        for i in range(len(self.__matrix)):
            result += f"x{i + 1}: | "
            row = self.__matrix[i]
            for point in row:
                result += str(point) + " | "
            result += "\n"
        return result
