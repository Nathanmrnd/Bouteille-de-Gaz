from .camions import Camion

class Plant :
    def __init__(self,x,y,capacity,init,refill):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.refill = refill
        self.stock = init

    def update_stock(self,t):
        self.stock += t*self.refill/24
        if self.stock > self.capacity :
            self.stock = self.capacity
        
    def give_bottle(self,Camion):
        self.stock -= (100 - Camion.bouteilles)


