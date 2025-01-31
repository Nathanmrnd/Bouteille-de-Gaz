import math
class Camions:
    def __init__(self,camion_id,bouteilles,x,y):
        self.camion_id=camion_id
        self.bouteilles=bouteilles
        self.x=x
        self.y=y

    def choisir_client_proche(self, clients):
        def distance(client):
            return math.sqrt((self.x - client.x) ** 2 + (self.y - client.y) ** 2)
        self.client_cible = min(clients, key=distance)
        
    def choisir_usine_proche(self,plants):
        def distance(plant):
            return math.sqrt((self.x - plant.x) ** 2 + (self.y - plant.y) ** 2)
        self.plant_cible = min(plants, key=distance)



camions = []
for usine in usines:
    for j in range(5):
        camions.append(
            Camion(
                id_camion=len(camions) + 1,  # ID unique pour chaque camion
                x=usine.x,
                y=usine.y
                bouteilles=100  # Nombre aléatoire de bouteilles
            )
        )