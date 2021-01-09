# Created 12/4/18
# Main file for our game

# import the pygame graphic module
import pygame

# import the game driver from game_driver
from game_driver import GameDriver

# set the window size to 750 by 750
screen = pygame.display.set_mode((750, 750))

# Adding window title
pygame.display.set_caption("Tron")

# ste the trail size to 5
SQUARE_SIZE = 5

# set the frames per second to 100
FPS = 75

# create an instance of GameDriver
driver = GameDriver(screen, SQUARE_SIZE)

# Set the repeat delay before pygame.KEYDOWN events are fired again
# Required when using enter to advance screens
# If not, pygame will register enter too quickly
pygame.key.set_repeat(1000, 100)


"""While exited is still False, check for whether the user exits the game, in which case, make exited True and 
exit the event loop, keep calling the add_event function. If exited is still False, make the screen white,
call the main game driver (driver.tick) and flip the graphics to the screen"""
exited = False
while not exited:
    # Wait 1000/FPS seconds, for a total of 1000 ms in a second :)
    pygame.time.delay(1000//FPS)

    # Clear the events
    driver.clear_events()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exited = True
            break

        # Add the event to the driver event list
        driver.add_event(event)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update the driver
    driver.tick()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
