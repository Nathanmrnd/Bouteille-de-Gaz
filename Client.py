class Client:
    """ Représente un client consommant des bouteilles de gaz. """
    def __init__(self, id, coord_x, coord_y, capacity, init, consumption):
        self.id = id
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.capacity = capacity
        self.stock_full = 0  # Bouteilles pleines stockées
        self.stock_empty = init  # Bouteilles vides accumulées
        self.consumption = consumption  # Consommation par jour

    def consume_gas(self):
        """ Consomme des bouteilles et génère des bouteilles vides. """
        consumed = min(self.stock_full, self.consumption)
        self.stock_full -= consumed
        self.stock_empty += consumed