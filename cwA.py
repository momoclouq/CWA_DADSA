import csv

from StoreA import StoreA
from StoreB import StoreB
from StoreC import StoreC
from Order  import Order
from Item   import Item


class Node:
    def __init__(self, data):
        self.item = data
        self.next = None  # reference to the next node
        self.pre = None  # reference to the previous node

class DoublyLinkedList:

    def __init__(self):  # when a new instance of the DLL is created, there is nothing in it
        self.start_node = None
    
    def initItemList(self):
       with open('shoplist.csv') as csv_file:
           reader = csv.reader(csv_file, delimiter=',')
           next(reader)
           for col in reader:
            tempItem= Item(col[1], col[2], col[3], col[4], col[5])
            item.insert(tempItem)
    
    def initStoreAList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for col in reader:
                tempStoreA = StoreA(col[1], col[3])
                if tempStoreA.check == "Y": 
                    storeA.insert(tempStoreA)
    
    def initStoreBList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for col in reader:
                tempStoreB = StoreB(col[1], col[4])
                if tempStoreB.check == "Y": 
                    storeB.insert(tempStoreB)
    
    def initStoreCList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for col in reader:
                tempStoreC = StoreC(col[1], col[5])
                if tempStoreC.check == "Y": 
                    storeC.insert(tempStoreC)
    
    def initOrderList(self):
        with open('householdlist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            
            
            tempitem = next(reader)
            tempitem.pop(0)
            
            
            row2 = next(reader)
                        
            
            b = 1
            c = 0
            item = []
            order1 = []
            tempOrder = []
            tempItem = []
            for col in reader:
                order1.append(col)
            
            while b<8:
                for x in order1:
                 
                    tempItem.append(x[0])
                    tempOrder.append(x[b])
                b= b+1
                
                tempHouse = Order(tempitem[c],tempItem, tempOrder)
                order.insert(tempHouse)
                
                c= c+1
                tempOrder = []
                tempItem  = []

    #def sortOrder(self)

    
    def itemSearch(self, value):
        x = False
        n = self.start_node
        head = n
        tail = n  
        while tail.next is not None:  
            tail = tail.next
        while head is not tail:
            if head.item.item == value or tail.item.item == value:
                x = True
                break
            else:
                head = head.next
                tail = tail.pre
        if x:
            if head.item.item == value:
                return head.item
            else:
                return tail.item
        else:
            return None

    def insert(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.pre = n
    
    def sortNodes(self):
        if self.start_node is None:
            return;
        else:
            current = self.start_node
            while current.next is not None:
                index = current.next
                while index is not None:
                    if (current.item > index.item):
                        temp = current.item
                        current.item = index.item
                        index.item = temp
                    index = index.next
                current = current.next
    
    def traverse(self):
        if self.start_node is None:
            print("List has no entry")
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.next
    
    def __str__(self): 
        
        # defining a blank res variable 
        res = "" 
          
        # initializing ptr to head 
        ptr = self.start_node 
          
       # traversing and adding it to res 
        while ptr: 
            res += str(ptr.item) + ", "
            ptr = ptr.next
  
       # removing trailing commas 
        res = res.strip(", ") 
          
        # chen checking if  
        # anything is present in res or not 
        if len(res): 
            return "[" + res + "]"
        else: 
            return "[]"


#shoplist = DoublyLinkedList()
#shoplist.initShopList()
item   = DoublyLinkedList()
storeA = DoublyLinkedList()
storeB = DoublyLinkedList()
storeC = DoublyLinkedList()
order  = DoublyLinkedList()

storeA.initStoreAList()
storeB.initStoreBList()
storeC.initStoreCList()
order.initOrderList()
item.initItemList()

#ans = input("Enter Order item: ")
#result = order.itemSearch(ans)
#a = result.itemlist
#b = result.order
#print(a + b) 

item.traverse()








    





