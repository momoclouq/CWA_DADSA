import csv

from allStore  import allStore
from Order  import Order




class Node:
    def __init__(self, data):
        self.item = data
        self.next = None  # reference to the next node
        self.pre = None  # reference to the previous node

class DoublyLinkedList:
    def __init__(self):  # when a new instance of the DLL is created, there is nothing in it
        self.head = None
        self.tail = None
    
    
    def initStoreList(self):
        with open('shoplist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            row1 = next(reader)

            tempItemA = []
            tempItemB = []
            tempItemC = []
            for col in reader:
                tempItem = col[1]
                if col[3] == "Y": 
                    tempItemA.append(tempItem)
                if col[4] == "Y": 
                    tempItemB.append(tempItem)
                if col[5] == "Y":
                    tempItemC.append(tempItem)
           
            
            tempStoreA = allStore(tempItemA, row1[3])
            tempStoreB = allStore(tempItemB, row1[4])
            tempStoreC = allStore(tempItemC, row1[5])
            store.insert(tempStoreA)
            store.insert(tempStoreB)
            store.insert(tempStoreC)
            
                    
    
    def initOrderList(self):
        with open('householdlist.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            
            #deal with first and second lines of file
            tempitem = next(reader) #take list of house numbers
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
            
            while b<8: #loop b<8 for first week
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
        n = self.head
        head = n
        tail = n  
        while tail.next is not None:  
            tail = tail.next
        while head is not tail:
            if head.item.name == value or tail.item.name == value:
                x = True
                break
            else:
                head = head.next
                tail = tail.pre
        if x:
            if head.item.name == value:
                return head.item
            else:
                return tail.item
        else:
            return None

    def insert(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.pre = n
    
    def sortNodes(self):
        if self.head is None:
            return;
        else:
            current = self.head
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
        if self.head is None:
            print("List has no entry")
        else:
            n = self.head
            while n is not None:
                print(n.item, " ")
                n = n.next
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.item.print),;    
            current = current.next;    
    
    #def check(self):
        

   

#shoplist = DoublyLinkedList()
#shoplist.initShopList()

order = DoublyLinkedList()
store = DoublyLinkedList()

order.initOrderList()
store.initStoreList()

#ans = input("Enter Store  : ")
#result = store.itemSearch(ans)


#b = result.order
#print(result)
#print(b)
#storeB.traverse()









    





