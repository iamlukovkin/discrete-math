from graph_interpretations.graph import Graph
from graph_interpretations.line import Line


class Incidence:
    __matrix: list
    __graph: Graph

    def __init__(self, matrix=None, graph=None):
        if graph is not None:
            self.set_graph(graph)
            self.set_matrix()
        elif matrix is not None:
            self.set_matrix(matrix)
            self.set_graph()

    def get_graph(self):
        if self.__graph.get_lines_count() == 0:
            self.set_graph()
        return self.__graph

    def set_graph(self, graph=None):
        if graph is not None:
            self.__graph = graph
        else:
            self.__set_graph()

    def set_matrix(self, matrix=None):
        if matrix is not None:
            self.__matrix = matrix
        else:
            self.__set_matrix()

    def __set_matrix(self):
        if self.__graph.get_lines_count() == 0:
            raise ValueError("Graph must have at least one line")
        self.__matrix = [[0 for _ in range(self.__graph.get_lines_count())]
                         for _ in range(self.__graph.get_points_count())]
        for i in range(self.__graph.get_lines_count()):
            line = self.__graph.get_lines()[i]
            if line.get_source() == line.get_target():
                self.__matrix[line.get_source()][i] = 2
            else:
                self.__matrix[line.get_source()][i] = 1
                self.__matrix[line.get_target()][i] = -1

    def __set_graph(self):
        if len(self.__matrix) == 0:
            raise ValueError("Matrix must not be empty")
        self.__graph = Graph()

        for i in range(len(self.__matrix[0])):
            relation = [row[i] for row in self.__matrix]
            if 2 in relation:
                point_index = relation.index(2)
                self.__graph.add_line(Line(point_index, point_index))
            else:
                point_index = relation.index(1)
                target_index = relation.index(-1)
                self.__graph.add_line(Line(point_index, target_index))

    def __str__(self):
        result = "Incidence matrix:\n"
        for i in range(len(self.__matrix)):
            line = self.__matrix[i]
            result += f"x{i + 1}: "
            for point in line:
                result += f"| {point}"
                if len(str(point)) == 1:
                    result += " "
            result += "|\n"
        return result
