class Graph:
    __lines: list

    def __init__(self):
        self.__lines = []

    def set_lines(self, lines):
        self.__lines = lines

    def get_lines(self):
        return self.__lines

    def get_lines_count(self):
        return len(self.__lines)

    def add_line(self, line):
        self.__lines.append(line)

    def __str__(self):
        result = ""
        for i, line in enumerate(self.__lines):
            result += f"{i + 1}: {str(line)}\n"
        return result

    def get_points_count(self):
        points = []
        for line in self.__lines:
            if line.get_source() not in points:
                points.append(line.get_source())
            if line.get_target() not in points:
                points.append(line.get_target())
        return len(points)
