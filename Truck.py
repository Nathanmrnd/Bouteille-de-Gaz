import math
<<<<<<< HEAD:Truck.py
class Truck:
    def __init__(self,truck_id,bouteilles,x,y):
        self.truck_id=truck_id
=======
class Camion:
    def __init__(self,camion_id,bouteilles,x,y):
        self.camion_id=camion_id
>>>>>>> a59bd6957ed4ff9ea5a6bae40e615ea04d2042f0:camions.py
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

    def load(self, quantity):
        """ Charge des bouteilles dans le camion. """
        if self.stock + quantity <= self.MAX_CAPACITY:
            self.stock += quantity
        else:
            self.stock = self.MAX_CAPACITY  # Chargement maximal

    def unload(self, quantity):
        """ Décharge des bouteilles du camion. """
        if self.stock - quantity >= 0:
            self.stock -= quantity
        else:
            self.stock = 0



