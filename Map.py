import numpy as np
import pygame

from globals import UP, DOWN, LEFT, RIGHT, WHITE, BLACK, GRAYBLUE


class DMap:
    def __init__(self):
        self.__width = 20
        self.__height = 20
        self.surface = np.zeros((self.__width, self.__height))
        for i in range(self.__width):
            for j in range(self.__height):
                self.surface[i][j] = -1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def markDetectedWalls(self, e, x, y):
        #   To DO
        # mark on this map the walls that you detect
        walls = e.readUDMSensors(x, y)
        if walls is None:
            return

        i = x - 1
        if walls[UP] > 0:
            while (i >= 0) and (i >= x - walls[UP]):
                self.surface[i][y] = 0
                i = i - 1
        if i >= 0:
            self.surface[i][y] = 1

        i = x + 1
        if walls[DOWN] > 0:
            while (i < self.__width) and (i <= x + walls[DOWN]):
                self.surface[i][y] = 0
                i = i + 1
        if i < self.__width:
            self.surface[i][y] = 1

        j = y + 1
        if walls[LEFT] > 0:
            while (j < self.__height) and (j <= y + walls[LEFT]):
                self.surface[x][j] = 0
                j = j + 1
        if j < self.__height:
            self.surface[x][j] = 1

        j = y - 1
        if walls[RIGHT] > 0:
            while (j >= 0) and (j >= y - walls[RIGHT]):
                self.surface[x][j] = 0
                j = j - 1
        if j >= 0:
            self.surface[x][j] = 1

        return None

    def image(self, x, y):

        imagine = pygame.Surface((420, 420))
        brick = pygame.Surface((20, 20))
        empty = pygame.Surface((20, 20))
        empty.fill(WHITE)
        brick.fill(BLACK)
        imagine.fill(GRAYBLUE)

        for i in range(self.__width):
            for j in range(self.__height):
                if self.surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
                elif self.surface[i][j] == 0:
                    imagine.blit(empty, (j * 20, i * 20))

        drona = pygame.image.load("drona.png")
        if x is not None and y is not None:
            imagine.blit(drona, (y * 20, x * 20))
        return imagine