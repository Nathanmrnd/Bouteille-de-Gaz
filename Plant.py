<<<<<<< HEAD:Plant.py
=======
from .camions import Camion

>>>>>>> a59bd6957ed4ff9ea5a6bae40e615ea04d2042f0:Usine.py
class Plant :
    def __init__(self,x,y,capacity,init,refill):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.refill = refill
        self.stock = init

    def update_stock(self,dt):
        self.stock += dt*self.refill/24
        if self.stock > self.capacity :
            self.stock = self.capacity
        
<<<<<<< HEAD:Plant.py
    # def fill_camion(self,Camion):
    #     self.
=======
    def give_bottle(self,Camion):
        self.stock -= (100 - Camion.bouteilles)


>>>>>>> a59bd6957ed4ff9ea5a6bae40e615ea04d2042f0:Usine.py
