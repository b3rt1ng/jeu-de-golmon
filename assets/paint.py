

class Brush:
    def __init__(self, size) -> None:
        self.__size = size

    @property
    def size(self) -> int:
        return self.__size