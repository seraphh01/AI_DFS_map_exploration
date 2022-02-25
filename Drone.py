import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT

from Map import DMap


class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stack = list()
        self.visited = list()
        self.path = list()

    def move(self, detected_map):
        pressed_keys = pygame.key.get_pressed()

        if self.x > 0:
            if pressed_keys[K_UP] and detected_map.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detected_map.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1

        if self.y > 0:
            if pressed_keys[K_LEFT] and detected_map.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < 19:
            if pressed_keys[K_RIGHT] and detected_map.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def adjacent_squares(self, map: DMap):
        if self.x is None or self.y is None:
            return []

        if self.x < 0 or self.y < 0:
            return []

        adjacent = []

        # With this the drone can travel diagonally
        #
        # for i in range(self.x - 1, self.x + 2):
        #     if i not in range(0, map.width):
        #         continue
        #     for j in range(self.y - 1, self.y + 2):
        #         if j not in range(0, map.height):
        #             continue
        #
        #         if map.surface[i][j] != 1:
        #             adjacent.append((i, j))

        for i in range(self.x - 1, self.x + 2):
            if i not in range(0, map.width):
                continue
            if map.surface[i][self.y] != 1:
                adjacent.append((i, self.y))

        for j in range(self.y - 1, self.y + 2):
            if j not in range(0, map.height):
                continue
            if map.surface[self.x][j] != 1:
                adjacent.append((self.x, j))
        if (self.x, self.y) in adjacent:
            adjacent.remove((self.x, self.y))
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
            self.x = pos[0]
            self.y = pos[1]
            return
        else:
            pos = (None, None)
            self.x = None
            self.y = None
            return

        # while pos in self.visited and len(self.stack) > 0:
        #      pos = self.stack.pop()
        #
        # if not self.in_range(pos):
        #     pos = self.path.pop()

        self.visit(*pos)
        self.path.append((self.x, self.y))
        self.x = pos[0]
        self.y = pos[1]

