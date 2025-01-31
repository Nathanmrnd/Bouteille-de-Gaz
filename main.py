from Truck import Truck
from Plant import Plant
from Client import Client

T = 0

clients = []
with open("clients.csv", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        infos = line.split(",")
        clients.append(Client(float(infos[0]),
                            float(infos[1]),
                            int(infos[2]),
                            int(infos[3]),
                            float(infos[4])
                        ))
plants = []
with open("plants.csv", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        infos = line.split(",")
        plants.append(Plant(float(infos[0]),
                            float(infos[1]),
                            int(infos[2]),
                            int(infos[3]),
                            float(infos[4])
                        ))
trucks = []
for plant in plants:
    for j in range(5):
        if len(trucks)<100:
            trucks.append(Truck(
                    truck_id=len(trucks) + 1,  # ID unique pour chaque camion
                    x=plant.x,
                    y=plant.y,
                    bouteilles=100
                ))
while True:
    dt = min(trucks, key = lambda x : x.time_to_destination)
    # update plants
    for plant in plants:
        plant.update_stock(dt)
    # update clients
    for client in clients:
        client.update_stock(dt)
    # update each truck
    for truck in trucks:
        truck.time_to_destination -= dt
        # for the truck that has arrived, then update plants/clients
        if truck.time_to_destination == 0:
            if type(truck.destination) == Plant:
                truck.load_at_plant()
            elif type(truck.destination) == Client:
                truck.unload_at_client()
            truck.choose_destination()