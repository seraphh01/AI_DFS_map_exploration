import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT

from domain.Drone import Drone
from domain.Map import DMap


class DroneController:
    def __init__(self, drone: Drone):
        self.__drone = drone
        self.stack = list()
        self.visited = list()
        self.path = list()
        pass

    def move(self, detected_map):
        pressed_keys = pygame.key.get_pressed()

        if self.__drone.x > 0:
            if pressed_keys[K_UP] and detected_map.surface[self.__drone.x - 1][self.__drone.y] == 0:
                self.__drone.x = self.__drone.x - 1
        if self.__drone.x < 19:
            if pressed_keys[K_DOWN] and detected_map.surface[self.__drone.x + 1][self.__drone.y] == 0:
                self.__drone.x = self.__drone.x + 1

        if self.__drone.y > 0:
            if pressed_keys[K_LEFT] and detected_map.surface[self.__drone.x][self.__drone.y - 1] == 0:
                self.__drone.y = self.__drone.y - 1
        if self.__drone.y < 19:
            if pressed_keys[K_RIGHT] and detected_map.surface[self.__drone.x][self.__drone.y + 1] == 0:
                self.__drone.y = self.__drone.y + 1

    def adjacent_squares(self, map: DMap):
        if self.__drone.x is None or self.__drone.y is None:
            return []

        if self.__drone.x < 0 or self.__drone.y < 0:
            return []

        adjacent = []

        # With this the drone can travel diagonally
        #
        # for i in range(self.__drone.x - 1, self.__drone.x + 2):
        #     if i not in range(0, map.width):
        #         continue
        #     for j in range(self.__drone.y - 1, self.__drone.y + 2):
        #         if j not in range(0, map.height):
        #             continue
        #
        #         if map.surface[i][j] != 1:
        #             adjacent.append((i, j))

        for i in range(self.__drone.x - 1, self.__drone.x + 2):
            if i not in range(0, map.width):
                continue
            if map.surface[i][self.__drone.y] != 1:
                adjacent.append((i, self.__drone.y))

        for j in range(self.__drone.y - 1, self.__drone.y + 2):
            if j not in range(0, map.height):
                continue
            if map.surface[self.__drone.x][j] != 1:
                adjacent.append((self.__drone.x, j))
        if (self.__drone.x, self.__drone.y) in adjacent:
            adjacent.remove((self.__drone.x, self.__drone.y))
        return adjacent

    def visit(self, x, y):
        if (x, y) not in self.visited:
            self.visited.append((x, y))
        pass

    def in_range(self, pos, map):
        return pos in self.adjacent_squares(map)

    def moveDSF(self, map: DMap):
        # TO DO!
        # rewrite this function in such a way that you perform an automatic
        # mapping with DFS

        k = 0
        for adjacent in self.adjacent_squares(map):
            if adjacent in self.visited or adjacent in self.path:
                continue
            if adjacent not in self.stack:
                self.stack.append(adjacent)
                k += 1

        if len(self.stack) > 0 and self.in_range(self.stack[len(self.stack) - 1], map):
            pos = self.stack.pop()
        elif k == 0 and len(self.path) > 0:
            pos = self.path.pop()
            self.__drone.x = pos[0]
            self.__drone.y = pos[1]
            return
        else:
            pos = (None, None)
            self.__drone.x = None
            self.__drone.y = None
            return

        # while pos in self.visited and len(self.stack) > 0:
        #      pos = self.stack.pop()
        #
        # if not self.in_range(pos):
        #     pos = self.path.pop()

        self.visit(*pos)
        self.path.append((self.__drone.x, self.__drone.y))
        self.__drone.x = pos[0]
        self.__drone.y = pos[1]
