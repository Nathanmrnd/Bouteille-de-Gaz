from truck import Truck, renvoyer_profit
from plant import Plant
from client import Client
from board import Board
import pygame
import time
import random

T = 0

clients = []
with open("clients.csv", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        infos = line.split(",")
        clients.append(Client(x=float(infos[0]),
                            y=float(infos[1]),
                            capacity=int(infos[2]),
                            init=int(infos[3]),
                            consumption=float(infos[4])
                        ))
plants = []
with open("plants.csv", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        infos = line.split(",")
        plants.append(Plant(y=float(infos[0]),
                            x=float(infos[1]),
                            capacity=int(infos[2]),
                            init=int(infos[3]),
                            refill=float(infos[4])
                        ))

trucks = []
for plant in plants:
    while len(trucks)<100:
        random_client = random.choice(clients)
        trucks.append(Truck(
                truck_id=len(trucks) + 1,  # ID unique pour chaque camion
                x=random_client.x,
                y=random_client.y
            ))

pygame.init()
screen = pygame.display.set_mode((1000, 750))
b = Board(screen)
b.draw_game(plants, clients, trucks)
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.update()

while T<24*30:
    truck_arriving = min(trucks, key = lambda x : x.time_to_destination)
    dt = truck_arriving.time_to_destination
    T += dt
    # update plants
    for plant in plants:
        plant.update_stock(dt)
    # update clients
    for client in clients:
        client.update_stock(dt)
    # update each truck
    for truck in trucks:
        if truck.time_to_destination > 0:
            truck.update(dt)
        else:
             # for the truck that has arrived, then update plants/clients
            if type(truck_arriving.destination) == Plant:
                truck_arriving.load_at_plant()
            elif type(truck_arriving.destination) == Client:
                truck_arriving.unload_at_client()
            truck_arriving.new_destination()

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()
        if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    exit()

    time.sleep(dt/100000) # dt en h mais bonne valeur en s pour pause
    b.draw_game(plants, clients, trucks)
    text_surface = my_font.render(f"{round(renvoyer_profit())}€, {round(T)}h", False, (0, 0, 0))
    screen.blit(text_surface, (0,0))
    pygame.display.update()
print(renvoyer_profit())