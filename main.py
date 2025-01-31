from truck import Truck
from plant import Plant
from client import Client
from board import Board
import pygame
import time

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
    for j in range(5):
        if len(trucks)<100:
            trucks.append(Truck(
                    truck_id=len(trucks) + 1,  # ID unique pour chaque camion
                    x=plant.x,
                    y=plant.y
                ))

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
b = Board(screen)
b.draw_game(plants, clients, trucks)
pygame.display.update()

while True:
    truck_arriving = min(trucks, key = lambda x : x.time_to_destination)
    dt = truck_arriving.time_to_destination
    T += dt # pas nécessaire
    # update plants
    for plant in plants:
        plant.update_stock(dt)
    # update clients
    for client in clients:
        client.update_stock(dt)
    # update each truck
    for truck in trucks:
        print(truck.destination, truck.time_to_destination)
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
                break
        if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    break

    print("Hello")
    b.draw_t(trucks)
    pygame.display.update()