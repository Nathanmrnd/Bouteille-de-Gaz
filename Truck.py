import math
class Truck:
    def __init__(self,truck_id,x,y,destination,destination_type):
        self.truck_id = truck_id
        self.full_bottles = 0
        self.empty_bottles = 0
        self.x = x
        self.y = y
        self.destination, self.time_to_destination = self.choose_destination(self)

    # def choisir_client_proche(self, clients):
    #     def distance(client):
    #         return math.sqrt((self.x - client.x) ** 2 + (self.y - client.y) ** 2)
    #     self.destination = min(clients, key=distance)
    #     self.destination_type = 'client'
        
    # def choisir_usine_proche(self,plants):
    #     def distance(plant):
    #         return math.sqrt((self.x - plant.x) ** 2 + (self.y - plant.y) ** 2)
    #     self.destination = min(plants, key=distance)
    #     self.destination_type = 'plant'

    def load_at_plant(self):
        if self.destination.stock >= 100-self.bouteilles:
            self.bouteilles = 100
            self.destination.stock -= 100-self.bouteilles
        else:
            self.bouteilles += self.destination.stock
            self.destination.stock = 0

    def unload_at_client(self,destination):
        if self.bouteilles >= (destination.capacity-destination.stock_full):
            self.bouteilles -= (destination.capacity-destination.stock_full)

    def new_destination(self):
        destination = usine[0]
        # renvoyer destination et temps de trajet jusqu'à destination
        return (destination, 10)


