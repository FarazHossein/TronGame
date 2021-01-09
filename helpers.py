# A file for any helper functions we use
# Created 12/4/18

import pygame

# Initialize the font module
pygame.font.init()

# this class will be used to render the text that will go onto the screen
class Renderer:
    def __init__(self, screen):
        # Initialize the pygame screen, for drawing in render_text
        self.screen = screen

    def render_text(self, text, size, position, colour):
        """ this method is used to contain the information necessary to blit the text onto the screen"""

        # these variables/ attributes store the font, size, color,  message, and location of text
        font = pygame.font.SysFont("Arial", size)
        text = font.render(text, True, colour)
        self.screen.blit(text, position)

