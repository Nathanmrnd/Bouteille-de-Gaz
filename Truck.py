import random
from plant import Plant
from client import Client


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
        self.x, self.y = self.destination.x, self.destination.y
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
        self.x, self.y = self.destination.x, self.destination.y
        # déchargement des bouteilles pleines
        if self.full_bottles + self.destination.full_bottles <= self.destination.capacity - 1:
            self.destination.full_bottles += self.full_bottles
            self.full_bottles = 0
        else:
            self.full_bottles = self.destination.full_bottles + self.full_bottles - (self.destination.capacity - 1)
            self.destination.full_bottles = self.destination.capacity - 1
        # chargement des bouteilles vides
        if self.empty_bottles + self.destination.empty_bottles <= 80:
            self.empty_bottles += self.destination.empty_bottles
            self.destination.empty_bottles = 0
        else:
            self.destination.empty_bottles = self.empty_bottles + self.destination.empty_bottles - 80
            self.empty_bottles = 80


    def new_destination(self):
        from main import clients, plants

        def distance(destination):
            """ Calcule la distance euclidienne entre le camion et une destination """
            return ((self.x - destination.x) ** 2 + (self.y - destination.y) ** 2) ** 0.5

        if self.full_bottles == 0:
            # 🔹 Aller à l'usine la plus proche qui a du stock
            available_plants = [p for p in plants if p.full_bottles > 0]
            if available_plants:
                self.destination = min(available_plants, key=distance)
            else:
                self.destination = None  # Aucun choix possible, le camion reste bloqué
        else:
            # 🔹 Aller au client qui a le plus besoin de bouteilles, en minimisant la distance
            needy_clients = [c for c in clients if c.full_bottles < c.capacity - 1]
            if needy_clients:
                self.destination = min(needy_clients, key=lambda c: distance(c) / (c.capacity - c.full_bottles + 1))
            else:
                self.destination = None  # Aucun client valide, le camion reste bloqué

        # Calcul du temps nécessaire pour atteindre la nouvelle destination
        if self.destination:
            self.time_to_destination = distance(self.destination) / 50  # Vitesse supposée de 50 km/h
        else:
            self.time_to_destination = float('inf')  # Camion bloqué


    def update(self, dt):
        self.x += (self.destination.x-self.x)*dt/self.time_to_destination
        self.y += (self.destination.y-self.y)*dt/self.time_to_destination
        self.time_to_destination -= dt