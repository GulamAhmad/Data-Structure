class Node: 
    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        self.previous = None
    def display(self):
        print(self.element)

class LinkedList: 
    def __init__(self):
        self.head = None
        self.size = 0
 
    def len(self):
        return self.size
    
    def get_head(self):
        return self.head
    
    def is_empty(self):
        return self.size == 0 
    
    def display(self):
        if self.size == 0:
            print("No element")
            return 
        first = self.head
        print(first.element.element)
        first = first.next
        while first:
            if type(first.element) == type(my_list.head.element):
                print(first.element.element)
                first = first.next
            print(first.element)
            first = first.next
            
    
    def add_head(self,e):
        self.head = Node(e)
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
            self.head.previous = None
            self.size -= 1
            
    def add_tail(self,e):
        new_value = Node(e)
        new_value.previous = self.get_tail()
        self.get_tail().next = new_value
        self.size += 1
        
    def find_second_last_element(self):
        if self.size >= 2:
            first = self.head 
            temp_counter = self.size -2
            while temp_counter > 0:
                first = first.next 
                temp_counter -= 1 
            return first
        else:
            print("Size not sufficient")  
        return None      
        
    def remove_tail(self):
        if self.is_empty():
            print("Empty Singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else: 
            Node = self.find_second_last_element()
            if Node:
                Node.next = None
                self.size -= 1
                
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
                
    
    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            linkedlist_value.head.previous = last_node
            self.size = self.size + linkedlist_value.size
        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size
            
l1 = Node('AHMAD')
my_list = LinkedList()
my_list.add_head(l1)
my_list.add_tail('PRITAM')
my_list.add_tail('SATYAM')
my_list.add_tail('JOHANUS')

my_list2 = LinkedList()
l2 = Node('VARUN')
my_list2.add_head(l2)
my_list2.add_tail('DHRUVIN')
my_list2.add_tail('SHRAVAN')
my_list2.add_tail('AMAN')
my_list.merge(my_list2)
my_list.display()
my_list.get_tail()
