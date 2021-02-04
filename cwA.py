import csv

from StoreA import StoreA
from StoreB import StoreB
from StoreC import StoreC
from House  import House


class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None  # reference to the next node
        self.pref = None  # reference to the previous node

class DoublyLinkedList:

    def __init__(self):  # when a new instance of the DLL is created, there is nothing in it
        self.start_node = None
    
   
    def initStoreAList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for col in reader:
                tempStoreA = StoreA(col[1], col[3])
                if tempStoreA.check == "Y": 
                    storeA.insert(tempStoreA)
    def initStoreBList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for col in reader:
                tempStoreB = StoreB(col[1], col[4])
                if tempStoreB.check == "Y": 
                    storeB.insert(tempStoreB)
    def initStoreCList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for col in reader:
                tempStoreC = StoreC(col[1], col[5])
                if tempStoreC.check == "Y": 
                    storeC.insert(tempStoreC)
    
    def initHouseList(self):
        with open('householdlist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            row1 = next(reader)
            next(reader)
            for a in row1:
                tempNumber = House(a, None, None)
                house.insert(tempNumber)
            count = 1   
            for col in reader:
                tempItem = House(None, col[0], None)
                house.insert(tempItem)
                
            while count < 7 :
                tempOrder = House(None, None, col[count])
                count += 1
                house.insert(tempOrder)
        

                     



            
    def nameSearch(self, value):
        x = False
        n = self.start_node
        head = n
        tail = n  
        while tail.nref is not None:  
            tail = tail.nref
        while head is not tail:
            if head.item.number == value or tail.item.number == value:
                x = True
                break
            else:
                head = head.nref
                tail = tail.pref
        if x:
            if head.item.number == value:
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
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n
    
    def sortNodes(self):
        if self.start_node is None:
            return;
        else:
            current = self.start_node
            while current.nref is not None:
                index = current.nref
                while index is not None:
                    if (current.item > index.item):
                        temp = current.item
                        current.item = index.item
                        index.item = temp
                    index = index.nref
                current = current.nref


#shoplist = DoublyLinkedList()
#shoplist.initShopList()

storeA = DoublyLinkedList()
storeB = DoublyLinkedList()
storeC = DoublyLinkedList()
house  = DoublyLinkedList()

storeA.initStoreAList()
storeB.initStoreBList()
storeC.initStoreCList()
house.initHouseList()

#ans = input("Enter house number: ")
#result = house.nameSearch(ans)
#print(result.print_all, " ")


node = linked_list.head
while node:
    print node.value
    node = node.next





    





