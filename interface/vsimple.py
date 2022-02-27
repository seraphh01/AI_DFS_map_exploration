# import the pygame module, so you can use it
import time

from random import randint

# Creating some colors
from controller.DroneController import DroneController
from domain.Drone import Drone
from domain.Environment import *

# define indexes variations
from domain.Map import DMap


# define a main function
def main():
    # we create the environment
    e = Environment()
    # e.randomMap()
    # e.saveEnvironment("test1.map")
    e.loadEnvironment("test2.map")

    # print(str(e))

    # we create the map
    m = DMap()

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("drone exploration")

    # we position the drone somewhere in the area
    x = randint(0, 19)
    y = randint(0, 19)

    x = 0
    y = 0

    # cream drona
    d = Drone(x, y)
    controller = DroneController(d)

    # create a surface on screen that has the size of 800 x 480
    screen = pygame.display.set_mode((800, 400))
    screen.fill(WHITE)
    screen.blit(e.image(), (0, 0))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # if event.type == KEYDOWN:
            #     # use this function instead of move
            #     d.moveDSF(m)
            #     # d.move(m)
        controller.moveDSF(m)
        time.sleep(0.01)
        m.markDetectedWalls(e, d.x, d.y)
        screen.blit(m.image(d.x, d.y), (400, 0))
        pygame.display.flip()

    pygame.quit()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
