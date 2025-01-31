import math
from main import clients, plants
import random

class Truck:
    def __init__(self,truck_id,x,y,destination,destination_type):
        self.truck_id = truck_id
        self.full_bottles = 0
        self.empty_bottles = 0
        self.x = x
        self.y = y
        self.destination, self.time_to_destination = None, None
        self.choose_destination(self)


    def load_at_plant(self):
        # chargement des bouteilles pleines
        if self.full_bottles + self.destination.full_bottles <= 80:
            self.full_bottles += self.destination.full_bottles
            self.destination.full_bottles = 0
        else:
            self.destination.full_bottles = self.destination.full_bottles + self.full_bottles - 80
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
        # déchargement des bouteilles pleines
        if self.full_bottles + self.destination.full_bottles <= self.destination.capacity - 1:
            self.destination.full_bottles += self.full_bottles
            self.full_bottles = 0
        else:
            self.full_bottles = self.destination.full_bottles + self.full_bottles - (self.destination.capacity - 1)
            self.destination.full_bottles = self.capacity - 1
        # chargement des bouteilles vides
        if self.empty_bottles + self.destination.empty_bottles <= 80:
            self.empty_bottles += self.destination.empty_bottles
            self.destination.empty_bottles = 0
        else:
            self.destination.empty_bottles = self.empty_bottles + self.destination.empty_bottles - 80
            self.empty_bottles = 80
        self.choose_destination(self)


    def new_destination(self):
        destination = random.choice(clients)
        if self.full_bottles == 0:
            destination = random.choice(plants)
        # renvoyer destination et temps de trajet jusqu'à destination
        def distance(self, destination):
            return ((self.x-destination.x)**2 + (self.y-destination.y)**2)**0.5
        self.destination = destination
        self.time_to_destination = distance(self, destination)/50