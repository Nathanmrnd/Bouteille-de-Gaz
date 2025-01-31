import math
class Truck:
    def __init__(self,truck_id,x,y,destination,destination_type):
        self.truck_id = truck_id
        self.full_bottles = 0
        self.empty_bottles = 0
        self.x = x
        self.y = y
        self.destination, self.time_to_destination = self.choose_destination(self)


    def load_at_plant(self):
        if self.full_bottles + self.destination.full_bottles <= 80:
            self.full_bottles += self.destination.full_bottles
            self.destination.full_bottles = 0
        else:
            self.destination.full_bottles = self.destination.full_bottles + self.full_bottles - 80
            self.full_bottles = 80

        if self.empty_bottles + self.destination.empty_bottles <= self.destination.capacity - 1: # pour la bouteille en cours de remplissage
            self.destination.empty_bottles += self.empty_bottles
            self.empty_bottles = 0
        else:
            self.empty_bottles = self.destination.empty_bottles + self.empty_bottles - (self.capacity - 1)
            self.destination.empty_bottles = self.destination.capacity - 1

        # Rq : les deux if ne peuvent pas être faux car sinon le camion ou l'usine déborderait déjà
        


    def unload_at_client(self,destination):
        if self.bouteilles >= (destination.capacity-destination.stock_full):
            self.bouteilles -= (destination.capacity-destination.stock_full)
            destination.stock = destination.capacity
        else:
            destination.stock = self.bouteilles+destination.stock_full
            self.bouteilles = 0


    def new_destination(self):
        destination = usine[0]
        # renvoyer destination et temps de trajet jusqu'à destination
        return (destination, 10)