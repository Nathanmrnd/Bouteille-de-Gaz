import math
class Camion:
    def __init__(self,camion_id,bouteilles,x,y,destination,typedestination):
        self.camion_id=camion_id
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

    def refill_truck(self):
        if self.destination.stock >= (100-self.bouteilles):
            self.bouteilles = 100
            self.destination.stock -= self.stock
        else:
            self.bouteilles += self.destination.stock
            self.destination.stock = 0



