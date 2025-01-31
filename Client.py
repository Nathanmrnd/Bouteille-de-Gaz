class Client:
    """ Représente un client consommant des bouteilles de gaz. """
    def __init__(self, coord_x, coord_y, capacity, init, consumption):
        self.x = coord_x
        self.y = coord_y
        self.capacity = capacity
        self.full_bottles = 0  # Bouteilles pleines stockées
        self.empty_bottles = init  # Bouteilles vides accumulées
        self.consumption = consumption  # Consommation par jour

    def update_stock(self,t_dest):
        self.full_bottles -= t_dest * self.consumption / 24 
        self.empty_bottles += t_dest * self.consumption / 24 
        if self.full_bottles < 0 :
            self.empty_bottles +=  self.full_bottles
            self.full_bottles = 0
