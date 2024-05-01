class Graph:
    __matrix: list[list[int]]

    def __init__(self, matrix: list[list[int]]) -> None:
        self.__matrix = matrix

    def get_matrix(self) -> list[list[int]]:
        return self.__matrix

    def set_matrix(self, matrix: list[list[int]]) -> None:
        self.__matrix = matrix

    def __str__(self):
        result: str = ""
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                result += str(self.__matrix[i][j]) + " "
            result += "\n"

    def find_min_edge(self, visited):
        """
        Поиск минимального ребра.
        Arg:
            visited (List[bool]): Список посещенных вершин.
        Returns:
            Tuple[int, int]: Минимальное ребро в виде кортежа (u, v).
        """
        min_weight = float('inf')
        min_edge = None
        vertices_count = len(self.__matrix)

        for i in range(vertices_count):
            if visited[i]:
                for j in range(vertices_count):
                    if not visited[j] and self.__matrix[i][j] != 0 and self.__matrix[i][j] < min_weight:
                        min_weight = self.__matrix[i][j]
                        min_edge = (i, j)

        return min_edge

    def get_minimal_tree_by_prim_algorithm(self):
        """
        Выполнение алгоритма Прима для построения минимального остовного дерева.
        """
        vertices_count: int = len(self.__matrix)
        minimal_tree: list = []
        visited = [False] * len(self.__matrix)
        visited[0] = True

        while len(minimal_tree) < vertices_count - 1:
            min_edge = self.find_min_edge(visited)
            if min_edge is None:
                break
            minimal_tree.append(min_edge)
            visited[min_edge[1]] = True
        return minimal_tree
