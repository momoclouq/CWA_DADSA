class Item:
 def __init__(self, name, cost, storeA, storeB, storeC):
    
    self.name = name
    self.cost = cost   
    self.storeA = storeA
    self.storeB = storeB
    self.storeC = storeC
    self.print_once = "Name: " + name + ", "+"Cost: "+ cost + ", "+"StoreA: " + storeA + ", "+"StoreB: " + storeB + ", "+"StoreC: " + storeC
    self.print_all = name + ", " + cost + ", " + storeA + ", " + storeB + ", "+ storeC