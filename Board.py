import pygame
from .Plant import Plant
from .Truck import Truck
from .Client import Client

class Board:
    def __init__(self,screen):
        self.color = (128,128,128)
        self.screen = screen

    def draw_plant(self,plant : Plant):
        rect = pygame.Rect(plant.x, plant.y, 10, 10)
        pygame.draw.rect(self.screen, (0,0,0) , rect)

    def draw_truck(self,truck: Truck):
        rect = pygame.Rect(truck.x, truck.y, 10, 10)
        pygame.draw.rect(self.screen, (255,0,0) , rect)

    def draw_client(self,client: Client):
        rect = pygame.Rect(client.coord_x, client.coord_x, 10, 10)
        pygame.draw.rect(self.screen, (255,0,0) , rect)


    def draw_game(self,plants,clients,trucks):
        self.screen.fill(self.color)
        for plant in plants:    
            self.draw_plant(plant)
        for client in clients:
            self.draw_client(client)
#peut-être réflechir à ne pas redessiner les usines/clients à chaque fois
        for truck in trucks:
            self.draw_truck(truck)

        pygame.display.update()

