import math
class Truck:
    def __init__(self,truck_id,bouteilles,x,y,destination,typedestination):
        self.truck_id=truck_id
        self.bouteilles=bouteilles
        self.x=x
        self.y=y
        self.destination=destination
        self.typedestination=typedestination

    def choisir_client_proche(self, clients):
        def distance(client):
            return math.sqrt((self.x - client.x) ** 2 + (self.y - client.y) ** 2)
        self.destination = min(clients, key=distance)
        self.typedestination = 'client'
        
    def choisir_usine_proche(self,plants):
        def distance(plant):
            return math.sqrt((self.x - plant.x) ** 2 + (self.y - plant.y) ** 2)
        self.destination = min(plants, key=distance)
        self.typedestination = 'plant'

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

    def refill(self,destination):
        if self.destination.stock >= 100-self.bouteilles:
            self.bouteilles = 100
            self.destination.stock -= 100-self.bouteilles
        else:
            self.bouteilles += self.destination.stock
            self.destination.stock = 0

    def empty(self,destination):
        if self.bouteilles >= (destination.capacity-destination.stock_full):
            self.bouteilles -= (destination.capacity-destination.stock_full)


