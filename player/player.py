from random import randint

class Player:
    def __init__(self):
        self.__name = f"Antoine"
        self.__alive = True
        self.__color = (randint(0,255), randint(0,255), randint(0,255))
        self.__size = 15
        self.__speed = 2
        self.__jump_power = 10
        self.__posx = 600
        self.__posy = 400

    @property
    def name(self) -> str:
        return self.__name

    @property
    def alive(self) -> bool:
        return self.__alive
    
    @property
    def color(self) -> tuple:
        return self.__color
    
    @property
    def size(self) -> int:
        return self.__size
    
    @size.setter
    def size(self, new_size) -> None:
        self.__size = new_size
    
    @property
    def speed(self) -> int:
        return self.__speed
    
    @property
    def jump_power(self) -> int:
        return self.__jump_power
    
    @property
    def posx(self) -> int:
        return self.__posx
    
    @posx.setter
    def posx(self, new_pose):
        self.__posx = new_pose

    @property
    def posy(self) -> int:
        return self.__posy
    
    @posy.setter
    def posy(self, new_pose):
        self.__posy = new_pose
    