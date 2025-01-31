from Truck import Truck
from Plant import Plant
from Client import Client

T = 0
t = 0.1 # en heures
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
                    1))
while True:
    T+=t # à termes, calculer le premier instant où un camion arrive
    print(t)
    # update each truck
    # see if trucks have arrived, then update plants/clients
