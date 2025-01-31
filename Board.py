import pygame
from plant import Plant
from truck import Truck
from client import Client

xmin, xmax = -500, 1000
ymin, ymax = 4300, 5000
width, height = 1000, 750
def transform_x(x):
    return (x-xmin)/(xmax-xmin)*width
def transform_y(y):
    return (ymax-y)/(ymax-ymin)*height
class Board:
    def __init__(self,screen):
        self.color = (128,128,128)
        self.screen = screen

    def draw_plant(self,plant : Plant):
        rect = pygame.Rect(transform_x(plant.x), transform_y(plant.y), 10, 10)
        pygame.draw.rect(self.screen, (255,0,0) , rect)

    def draw_truck(self,truck: Truck):
        rect = pygame.Rect(transform_x(truck.x), transform_y(truck.y), 2, 2)
        pygame.draw.rect(self.screen, (0,255,0) , rect)

    def draw_client(self,client: Client):
        rect = pygame.Rect(transform_x(client.x), transform_y(client.y), 5, 5)
        pygame.draw.rect(self.screen, (0,0,255) , rect)


    def draw_game(self,plants,clients,trucks):
        self.screen.fill(self.color)
        for plant in plants:    
            self.draw_plant(plant)
        for client in clients:
            self.draw_client(client)
        for truck in trucks:
            self.draw_truck(truck)


    def draw_t(self,trucks):
        for truck in trucks:
            self.draw_truck(truck)

