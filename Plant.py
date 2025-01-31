from Truck import Truck

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
        
    def give_bottles(self,Truck):
        self.stock -= (100 - Truck.bouteilles)
        if self.stock < 0 :
            self.stock = 0


    def draw_plant(self):
        rect = pygame.Rect(self.x, self.y, 10, 10)


    