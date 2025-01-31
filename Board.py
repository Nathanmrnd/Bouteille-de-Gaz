import pygame

class Board:
    def __init__(self,screen):
        self.color = (128,128,128)
        self.screen = screen

    def draw_game(self,plants):
        self.screen.fill(self.color)
        for plant in plants:
            plant.draw_plant()

