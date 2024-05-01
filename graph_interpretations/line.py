# src/main/models/line.py
class Line:
    __source: int
    __target: int

    def __init__(self, source, target):
        self.set_source(source)
        self.set_target(target)

    def set_source(self, source):
        if source < 0:
            raise ValueError()
        self.__source = source

    def set_target(self, target):
        if target < 0:
            raise ValueError()
        self.__target = target

    def get_source(self):
        return self.__source

    def get_target(self):
        return self.__target

    def get_points(self):
        return [self.__source, self.__target]

    def __str__(self):
        return f"Line {{source={self.get_source() + 1}; target={self.get_target() + 1}}}"
