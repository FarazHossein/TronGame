# a file to load and manage images
# created 12/4/2018

import pygame

"""Create a class for the grahpics. These are simply attributes that will be called for in the main game driver,
"game_driver"""""
class Graphics:
    def __init__(self, screen, SQUARE_SIZE):
        # The screen width and height
        self.width = screen.get_width()
        self.height = screen.get_height()

        self.screen = screen

        # these two attributes call the image for the grid the players will see when they are playing the game
        self.main_background = pygame.image.load("images\\Tron_Background.png")
        self.main_background = pygame.transform.scale(self.main_background, (self.width, self.height))

        # The initial background
        self.init_background = pygame.image.load("images\\FirstScreen.png")
        self.init_background = pygame.transform.scale(self.init_background, (self.width, self.height))

        # The instruction screen
        self.Instructions_Screen = pygame.image.load("images\\InstructionsScreen.jpg")
        self.Instructions_Screen = pygame.transform.scale(self.Instructions_Screen, (self.width, self.height))

        # The Win Screens
        self.BlueWin = pygame.image.load("images\\BlueTronWinsBackground.png")
        self.BlueWin = pygame.transform.scale(self.BlueWin, (self.width, self.height))

        self.CyanWin = pygame.image.load("images\\CyanTronWinsBackground.png")
        self.CyanWin = pygame.transform.scale(self.CyanWin, (self.width, self.height))

        self.GreenWin = pygame.image.load("images\\GreenTronWinsBackground.png")
        self.GreenWin = pygame.transform.scale(self.GreenWin, (self.width, self.height))

        self.RedWin = pygame.image.load("images\\RedTronWinsBackground.png")
        self.RedWin = pygame.transform.scale(self.RedWin, (self.width, self.height))

        self.YellowWin = pygame.image.load("images\\YellowTronWinsBackground.png")
        self.YellowWin = pygame.transform.scale(self.YellowWin, (self.width, self.height))

        # The Bike images
        self.bikeB = pygame.image.load("images\\Blue.png")
        self.bikeB = pygame.transform.scale(self.bikeB, (SQUARE_SIZE * 10, SQUARE_SIZE  * 5))

        # these two attributes will call the image for the bike for player 2
        self.bikeC = pygame.image.load("images\\Cyan.png")
        self.bikeC = pygame.transform.scale(self.bikeC, (SQUARE_SIZE * 10, SQUARE_SIZE * 5))

        # these two attributes will call the image for the green bike
        self.bikeG = pygame.image.load("images\\Green.png")
        self.bikeG = pygame.transform.scale(self.bikeG, (SQUARE_SIZE * 10, SQUARE_SIZE * 5))

        # these two attributes will call the image for the red bike
        self.bikeR = pygame.image.load("images\\Red.png")
        self.bikeR = pygame.transform.scale(self.bikeR, (SQUARE_SIZE * 10, SQUARE_SIZE * 5))

        # these two attributes will call the image for the yellow bike
        self.bikeY = pygame.image.load("images\\Yellow.png")
        self.bikeY = pygame.transform.scale(self.bikeY, (SQUARE_SIZE * 10, SQUARE_SIZE * 5))

        # these two attributes call the draw background
        self.Tie = pygame.image.load("images\\Draw.png")
        self.Tie = pygame.transform.scale(self.Tie, (self.width, self.height))

        # A list of the colours, bikes and win images
        self.colour_list = [
            [(0, 0, 255), self.bikeB, self.BlueWin],
            [(0, 128, 255), self.bikeC, self.CyanWin],
            [(0, 255, 0), self.bikeG, self.GreenWin],
            [(255, 0, 0), self.bikeR, self.RedWin],
            [(255, 255, 0), self.bikeY, self.YellowWin]
        ]

        # Load the icon
        self.icon = pygame.image.load("images\\TronIcon.jpg")
