class Store:
    #Constructors
    def __init__(self, item, name):
        #items will not be duplicated, this is enforced by the user
        self.item = []
        self.name = name
    
    #method for usage
    def checkInStore(item):
        #check if item is in the store
        #use binary search, based on the fact that the items are sorted
        return binary_search(0, self.item.len(), item)

    def sortStore():
        #sort the items in the store for faster searching (binary search)
        return;

    
    ############################
    #algorithm methods

    def binary_search(self, low, high, x):
    #Recursive case
        if (high >= low):
            mid = (high + low) // 2
    
            #If element is at the middle -> found the value
            if self.item[mid] == x:
                return True
            #If element is smaller than the middle value -> search in the lower half
            elif self.item[mid] > x:
                return binary_search(arr, low, mid - 1, x)
            #If element is larger than the middle value -> search in the upper half
            else:
                return binary_search(arr, mid + 1, high, x)
            
        else:
            # Element is not present in the array
            return False


    def quick_sort():
        return;

    
    