class GraphColorer:
    __matrix: list

    def __init__(self, matrix):
        self.__matrix = matrix

    def __is_safe_vertex(self, vertex, color, colors):
        for i in range(len(self.__matrix)):
            if self.__matrix[vertex][i] == 1 and colors[i] == color:
                return False
        return True

    def __color_graph_helper(self, vertex, colors, num_colors=2):
        if vertex == len(self.__matrix):
            return True
        for color in range(1, num_colors + 1):
            if self.__is_safe_vertex(vertex, color, colors):
                colors[vertex] = color
                if self.__color_graph_helper(vertex + 1, colors):
                    return True
                colors[vertex] = 0
        return False

    def get_colors(self, num_colors):
        colors = [0] * len(self.__matrix)
        if self.__color_graph_helper(0, colors, num_colors):
            return colors
        else:
            return None
