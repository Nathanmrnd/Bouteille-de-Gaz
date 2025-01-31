import pygame
from plant import Plant
from truck import Truck
from client import Client

yoffset = 4000
class Board:
    def __init__(self,screen):
        self.color = (128,128,128)
        self.screen = screen

    def draw_plant(self,plant : Plant):
        rect = pygame.Rect(plant.x, plant.y-yoffset, 10, 10)
        pygame.draw.rect(self.screen, (0,0,0) , rect)

    def draw_truck(self,truck: Truck):
        rect = pygame.Rect(truck.x, truck.y-yoffset, 2, 2)
        pygame.draw.rect(self.screen, (255,0,0) , rect)

    def draw_client(self,client: Client):
        rect = pygame.Rect(client.x, client.y-yoffset, 5, 5)
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

