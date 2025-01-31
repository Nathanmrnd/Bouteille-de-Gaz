import random
from plant import Plant
from client import Client
profit = 0

def renvoyer_profit():
    return profit

class Truck:
    def __init__(self,truck_id,x,y):
        self.truck_id = truck_id
        self.full_bottles = 0
        self.empty_bottles = 0
        self.x = x
        self.y = y
        self.destination, self.time_to_destination = None, None
        self.new_destination()

    def load_at_plant(self):
        global profit
        self.x, self.y = self.destination.x, self.destination.y
        # chargement des bouteilles pleines
        if self.full_bottles + self.destination.full_bottles <= 80:
            profit-=40*self.destination.full_bottles
            self.full_bottles += self.destination.full_bottles
            self.destination.full_bottles = 0
        else:
            self.destination.full_bottles = self.destination.full_bottles + self.full_bottles - 80
            profit+=(self.full_bottles-80)*40
            self.full_bottles = 80
        # déchargement des bouteilles vides
        if self.empty_bottles + self.destination.empty_bottles <= self.destination.capacity - 1: # pour la bouteille en cours de remplissage
            self.destination.empty_bottles += self.empty_bottles
            self.empty_bottles = 0
        else:
            self.empty_bottles = self.destination.empty_bottles + self.empty_bottles - (self.destination.capacity - 1)
            self.destination.empty_bottles = self.destination.capacity - 1

        # Rq : les deux if ne peuvent pas être faux car sinon le camion ou l'usine déborderait déjà
        
    def unload_at_client(self):
        global profit
        self.x, self.y = self.destination.x, self.destination.y
        # déchargement des bouteilles pleines
        if self.full_bottles + self.destination.full_bottles <= self.destination.capacity - 1:
            self.destination.full_bottles += self.full_bottles
            profit+=self.full_bottles*100
            self.full_bottles = 0
        else:
            self.full_bottles = self.destination.full_bottles + self.full_bottles - (self.destination.capacity - 1)
            profit+=(self.destination.capacity-1-self.destination.full_bottles)*100
            self.destination.full_bottles = self.destination.capacity - 1
        # chargement des bouteilles vides
        if self.empty_bottles + self.destination.empty_bottles <= 80:
            self.empty_bottles += self.destination.empty_bottles
            self.destination.empty_bottles = 0
        else:
            self.destination.empty_bottles = self.empty_bottles + self.destination.empty_bottles - 80
            self.empty_bottles = 80


    def new_destination(self):
        global profit
        from main import clients, plants

        def distance(destination):
            return ((self.x - destination.x) ** 2 + (self.y - destination.y) ** 2) ** 0.5

        if self.full_bottles == 0:
            self.destination = max(plants, key = lambda plant : min(80, plant.full_bottles)/max(distance(plant), 0.01))
        else:
            self.destination = max(clients, key = lambda client : min(self.full_bottles, client.capacity-client.full_bottles)/max(distance(client), 0.01))
        
        # LE CODE SACRE'
        self.destination = random.choice(clients)
        if self.full_bottles == 0:
            self.destination = random.choice(plants)

        # Calcul du temps nécessaire pour atteindre la nouvelle destination
        self.time_to_destination = distance(self.destination) / 50  # Vitesse supposée de 50 km/h
        profit-=distance(self.destination)*0.1


    def update(self, dt):
        self.x += (self.destination.x-self.x)*dt/self.time_to_destination
        self.y += (self.destination.y-self.y)*dt/self.time_to_destination
        self.time_to_destination -= dt