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
        self.color = (128, 128, 128)
        self.screen = screen

    def draw_plant(self,plant : Plant, ratio):
        rect = pygame.Rect(transform_x(plant.x), transform_y(plant.y), 20, 20)
        pygame.draw.rect(self.screen, (255, 0, 0, 255*ratio) , rect)

    def draw_truck(self,truck: Truck, ratio):
        rect = pygame.Rect(transform_x(truck.x), transform_y(truck.y), 5, 5)
        pygame.draw.rect(self.screen, (0, 255, 100, 255*ratio) , rect)

    def draw_client(self,client: Client, ratio):
        rect = pygame.Rect(transform_x(client.x), transform_y(client.y), 5, 5)
        # print(ratio)
        pygame.draw.rect(self.screen, (0, 0, 255, 255*ratio) , rect)

    def draw_game(self,plants,clients,trucks):
        self.screen.fill(self.color)
        for plant in plants:    
            self.draw_plant(plant, plant.full_bottles/plant.capacity)
        for client in clients:
            self.draw_client(client, client.full_bottles/client.capacity)
        for truck in trucks:
            self.draw_truck(truck, truck.full_bottles/80)

        