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
        pass
        # if self.destination.stock >= 100-self.bouteilles:
        #     self.bouteilles = 100
        #     self.destination.stock -= 100-self.bouteilles


    def unload_at_client(self,destination):
        pass
        # if self.bouteilles >= (destination.capacity-destination.stock_full):
        #     self.bouteilles -= (destination.capacity-destination.stock_full)
        #     destination.stock = destination.capacity
        # else:
        #     destination.stock = self.bouteilles+destination.stock_full
        #     self.bouteilles = 0


    def new_destination(self):
        destination = usine[0]
        # renvoyer destination et temps de trajet jusqu'à destination
        return (destination, 10)