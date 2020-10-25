##link list with insertion deletion searching options...
class Node: 

    def _init_ (self, element, next = None ):
        self.element = element
        self.next = next
    def display(self):
        print(self.element)

class LinkedList:
        
    def _init_(self):
        self.head = None
        self.size = 0
        
 
        
    def _len_(self):
        return self.size
    
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size == 0:
            print("No element")
            return 
        first = self.head
        print(first.element)
        first = first.next
        while first:
            
            print(first.element)
            first = first.next
    
    
    def add_head(self,e):
        temp = self.head 
        self.head = Node(e) 
        self.head.next = temp
        self.size += 1 
        
    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object
        
    
    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.size -= 1
            
    def add_tail(self,e):
        new_value = Node(e)
        self.get_tail().next = new_value
        self.size += 1
                
    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index == 0:
            return element_node.element
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node
        
    def search (self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            print("Searching at " + str(index) + " and value is " + str(value.element))
            if value.element == search_value:
                print("Found value at " + str(index) + " location")
                return True
            index += 1
        print("Not Found")
        return False
    
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            self.size = self.size + linkedlist_value.size
            
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size

