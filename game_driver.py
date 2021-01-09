# File for our game driver class
# Created 12/4/18

# TODO: Comment

import pygame

from helpers import Renderer
from player import Player
from images import Graphics

"""we created a class for the main game, this class contains the code for when the instructions screen is displayed to 
the user, when the players control their bikes and they collide, when the game ends, and a function that calls the 
previously mentioned functions (for efficiency)"""


# This class is responsible for the game mechanics and the instructions to the user
class GameDriver:
    def __init__(self, screen, SQUARE_SIZE):
        # Storing our screen object
        self.screen = screen

        # Store our events in our list
        self.events = []

        # Initialize our square size
        self.SQUARE_SIZE = SQUARE_SIZE

        # Load our text renderer
        self.renderer = Renderer(screen)

        # Load our graphics module
        self.graphics = Graphics(screen, SQUARE_SIZE)

        # Our game driver state. It gets changed depending on what phase of the game we are on
        self.state = "init"

        # The victory verdict, set later
        self.verdict = ""

        # These variables are for controlling the colour changing screen
        self.selected_player = 1
        self.colour_warning = False

        # Rock out to MUSIC
        pygame.mixer.init()
        pygame.mixer.music.load("sound-files\\tron-music.mp3")
        pygame.mixer.music.play(-1)

        # Change the window icon
        pygame.display.set_icon(self.graphics.icon)

        # this creates an instance of the player class in "player.py", for the first player
        self.player1 = Player(self.screen, [pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d], (1, 0), (50, 375),
                              self.SQUARE_SIZE, *self.graphics.colour_list[0])

        # this creates an instance of the player class in "player.py", for the second player
        self.player2 = Player(self.screen, [pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT], (-1, 0),
                              (700, 375), self.SQUARE_SIZE, *self.graphics.colour_list[1])

    def tick_init(self):
        """this method will be used for when the user initially runs the game. This will be the first screen they see
        this lets the player know that they are playing "Tron" """
        # blit the image that is in the function "init_background"
        self.screen.blit(self.graphics.init_background, (0, 0))

        # Render the title
        # self.renderer.render_text("TRON", 300, (25, 200), (24, 202, 230))

        for ev in self.events:
            # Advance the state of the driver if the user pressed return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                self.state = "instructions"

    def tick_instructions(self):
        """ this method will be used to display the instructions onto the screen"""
        self.screen.blit(self.graphics.Instructions_Screen, (0, 0))

        for ev in self.events:
            # Advance the state of the driver if the user pressed return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                self.state = "colour"

    def tick_colour(self):
        # Render the text in the colour changing phase
        if self.colour_warning:
            self.renderer.render_text("You must choose different colours.", 50, (50, 500), (0, 0, 0))
        self.renderer.render_text("Player %d Colour Selection" % self.selected_player, 70, (75, 50), (0, 0, 0))
        self.renderer.render_text("Please Press Keys 1-5 To Select Colour", 35, (110, 135), (0, 0, 0))
        self.renderer.render_text("Press Enter To Confirm Selection", 35, (145, 175), (0, 0, 0))

        # Render the player 1 side
        self.renderer.render_text("Player 1 - ", 30, (50, 300), (0, 0, 0))  # showing player what colour they are
        self.screen.blit(self.player1.image, (180, 308))
        for p in range(5):
            self.renderer.render_text(str(p + 1), 30, (70 + 50 * p, 360), (0, 0, 0))  # showing possible colours
            self.screen.blit(self.graphics.colour_list[p][1], (50 + 50 * p, 400))

        # Render the player 2 side
        self.renderer.render_text("Player 2 - ", 30, (430, 300), (0, 0, 0))  # showing player what colour they are
        self.screen.blit(self.player2.image, (560, 308))
        for o in range(5):
            self.renderer.render_text(str(o + 1), 30, (450 + 50 * o, 360), (0, 0, 0))  # showing possible colours
            self.screen.blit(self.graphics.colour_list[o][1], (430 + 50 * o, 400))

        for ev in self.events:
            # Advance the state of the driver if the user pressed return
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    self.selected_player += 1

                # Update the colour if key 1-5 have been pressed
                for i in range(5):
                    if ev.key == getattr(pygame, "K_%d" % (i + 1)):
                        if self.selected_player == 1:
                            self.player1.update_colour(*self.graphics.colour_list[i])
                        else:
                            self.player2.update_colour(*self.graphics.colour_list[i])

        if self.selected_player == 3:
            # If they have the same colour, dont advance the state of the driver
            if self.player1.image == self.player2.image:
                self.selected_player -= 1
                self.colour_warning = True
                return

            # Otherwise, reset the selected player and warning and initialize the main phase
            self.colour_warning = False
            self.selected_player = 1
            self.state = "main"

    def tick_main(self):
        """ this method will be responsible for keeping track of whether there is a collision between players"""
        # Add the backgruond
        self.screen.blit(self.graphics.main_background, (0, 0))

        # Update both players
        self.player1.tick()
        self.player2.tick()

        # Check collisions
        collide1 = self.player1.collides(self.player2)
        collide2 = self.player2.collides(self.player1)

        # if the two players collide head-on, the game is a tie
        if collide1 and collide2:
            self.state = "game_end"
            self.verdict = "tie"

        # if the player 1 bike collides into the player 2 line, then player 2 wins
        elif collide1:
            self.state = "game_end"
            self.verdict = "win2"

        # if the player 2 bike collides into the player 1 line, then player 1 wins
        elif collide2:
            self.state = "game_end"
            self.verdict = "win1"

    def tick_game_end(self):
        """this function is used to display the messages when the game ends"""

        # Re-initialize players to be empty
        self.player1.re_init()
        self.player2.re_init()

        # Render the win images onto the screen
        if self.verdict == "win1":
            self.screen.blit(self.player1.win_image, (0, 0))

        if self.verdict == "win2":
            self.screen.blit(self.player2.win_image, (0, 0))

        # if the game ends in a tie, display the tie image onto the screen
        if self.verdict == "tie":
            self.screen.blit(self.graphics.Tie, (0, 0))

        # Reset to instructions if they press return
        for ev in self.events:
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                self.state = "instructions"

    def tick(self):
        """ this function will be used to call all the previous functions (for code efficiency)"""

        # if the games is at the home screen phase, call tick_init
        if self.state == "init":
            self.tick_init()

        # if the game is a t the instructions phase, call tick_instructions
        elif self.state == "instructions":
            self.tick_instructions()

        elif self.state == "colour":
            self.tick_colour()

        # if the game is at the gameplay phase, call tick_main
        elif self.state == "main":
            self.tick_main()

        # if the game is at the ending phase, call tick_game_end
        elif self.state == "game_end":
            self.tick_game_end()

    # Add the event to the events list
    def add_event(self, event):
        self.events.append(event)

    # Clear our events
    # Called every frame to reset the event list
    def clear_events(self):
        self.events.clear()
