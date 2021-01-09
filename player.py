# A file for our player class
# Created 12/4/18

import pygame
from images import Graphics

# this class is used to create the frame for the player. We will create instances of this class for each player
class Player:
    # Give it a pygame screen to draw to
    # Give it an array of movement keys
    # Order of movement keys is (left, up, down, right)
    # This should be passed as pygame.K_A, pygame.K_W, etc.
    def __init__(self, screen, keys, initial_direction, initial_position, square_size, colour, image, win_image):

        self.graphics = Graphics(screen, square_size)

        # Initialize the win image and bike image
        self.win_image = win_image
        self.image = image

        # Rotate the images
        self.left_image = self.image
        self.right_image = pygame.transform.rotate(self.left_image, 180)
        self.down_image = pygame.transform.rotate(self.left_image, 90)
        self.up_image = pygame.transform.rotate(self.left_image, 270)

        # this attribute contains the screen properties
        self.screen = screen

        # this attribute contains command for the key press tracker
        self.keys = keys

        # this list contains all of the coordinates for the trail
        self.tail = []

        # this attribute contains the direction of the bike
        self.direction = initial_direction

        # these two attributes contain the position and direction of the bike
        self.initial_position = initial_position
        self.initial_direction = initial_direction

        # Must be list so we can modify values
        # these attributes are used to store the position of the trail, and the properties of the trail
        self.head = list(initial_position)
        self.square_size = square_size
        self.tail_colour = colour

    def update_colour(self, colour, image, win_image):
        """ Update the colour of this player"""
        self.win_image = win_image
        self.tail_colour = colour
        self.image = image

        # Rotate the image
        self.left_image = self.image
        self.right_image = pygame.transform.rotate(self.left_image, 180)
        self.down_image = pygame.transform.rotate(self.left_image, 90)
        self.up_image = pygame.transform.rotate(self.left_image, 270)

    def re_init(self):
        """ this method re-initialize the player's position and direction """

        # Re-initialize player
        self.head = list(self.initial_position)
        self.direction = self.initial_direction

        # Reset the image
        self.image = self.left_image

        # Clear the tail of all its entries
        self.tail.clear()

    def update(self):
        """ this method is used to update the player's direction of movement"""

        # Get the keys
        left, up, down, right = self.keys

        # Get the pressed keys
        keys = pygame.key.get_pressed()

        # Update the direction if the direction is not opposite the current direction
        if keys[left] and self.direction != (1, 0):
            self.direction = (-1, 0)

        elif keys[up] and self.direction != (0, 1):
            self.direction = (0, -1)

        elif keys[down] and self.direction != (0, -1):
            self.direction = (0, 1)

        elif keys[right] and self.direction != (-1, 0):
            self.direction = (1, 0)

        # Update the image based on the direction
        if self.direction == (-1, 0):
            self.image = self.left_image

        elif self.direction == (1, 0):
            self.image = self.right_image

        elif self.direction == (0, -1):
            self.image = self.up_image

        elif self.direction == (0, 1):
            self.image = self.down_image

    def move(self):
        """ this method is used to keep of the coordinates of the trail"""

        # Must access the elements and put into array
        # Need to copy the list basically
        self.tail.append([self.head[0], self.head[1]])

        # change the value of self head, by the current value, multiplied by the size of the trail square
        self.head[0] += self.direction[0] * self.square_size
        self.head[1] += self.direction[1] * self.square_size

    def draw(self):
        """ this method will be used to draw the actual trail using the information above"""

        # create a loop that draws the actual trail
        for square in self.tail:
            pygame.draw.rect(self.screen, self.tail_colour, (square, (self.square_size, self.square_size)))

        # Draw the image based on the direction
        if self.direction == (-1, 0):  # left
            self.screen.blit(self.image, (self.head[0] - 3, self.head[1] - 9))

        elif self.direction == (0, -1):  # up
            self.screen.blit(self.image, (self.head[0] - 10, self.head[1] - 3))

        elif self.direction == (0, 1):  # down
            self.screen.blit(self.image, (self.head[0] - 9, self.head[1] - 40))

        elif self.direction == (1, 0):  # right
            self.screen.blit(self.image, (self.head[0] - 40, self.head[1] - 9))

    def tick(self):
        """ this method is used to call all the methods each frame for the player """

        self.update()
        self.move()
        self.draw()

    def collides(self, other):
        """this method is used to keep track of the collisions of the bikes"""

        # Check for collision with other player
        if self.head in other.tail:
            return True

        if self.head == other.head:
            return True

        # Check for collision with self
        if self.head in self.tail:
            return True

        # Check for collision with side of screen
        if self.head[0] > (self.screen.get_width() - 5) or self.head[0] < 0:
            return True

        if self.head[1] > self.screen.get_height() or self.head[1] < 0:
            return True

        return False
