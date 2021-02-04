class Item:
 def __init__(self, id, name, cost, storeA, storeB, storeC):
    self.id = id
    self.name = name
    self.cost = cost   
    self.storeA = storeA
    self.storeB = storeB
    self.storeC = storeC
    self.print_all = name + ',' + cost 