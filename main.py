from Truck import Truck
from Plant import Plant

T = 0
t = 0.1 # en heures
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
                    id_truck=len(trucks) + 1,  # ID unique pour chaque camion
                    x=plant.x,
                    y=plant.y,
                    bouteilles=100
                ))
while True:
    T+=t # à termes, calculer le premier instant où un camion arrive
    # update each truck
    # see if trucks have arrived, then update plants/clients
