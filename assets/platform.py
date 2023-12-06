import pygame

class Platform:
    def __init__(self, x, y, width, height, color = (0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.__color = color

    @property
    def color(self):
        return self.__color

class Cube(Platform):
    def __init__(self, x, y, width, color = (0,0,0)):
        super().__init__(x, y, width, width, color)