class Plant :
    def __init__(self,x,y,capacity,init,refill):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.refill = refill
        self.full_bottles = init
        self.empty_bottles = 0

    def update_stock(self,t_dest):#revoir nom variable
        if self.empty_bottles - t_dest*self.refill/24 > 0:
            self.full_bottles += t_dest*self.refill/24
            self.empty_bottles -= t_dest*self.refill/24
        else :
            self.full_bottles += self.empty_bottles
            self.empty_bottles =0
        




        


    