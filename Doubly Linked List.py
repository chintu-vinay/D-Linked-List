class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        curr = self.head
        if(not curr):
            print('Their are no elements to print in the doubly linked list')
        else:
            while(curr):
                print(curr.value)
                curr = curr.next
    
    def make_empty(self):
        self.tail.prev = self.head.next = None
        self.tail = self.head = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if(not self.head):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print('The appended element is ', value)
        self.length += 1
    
    def pop(self, ope = 'poped'):
        if(not self.head):
            print('Their are no elements to pop from doubly linked list')
            return False
        elif(self.length == 1):
            print(f'The {ope} element in the doubly lined list is ', self.tail.value)
            self.tail = self.head = None
            if(ope != 'poped'):
                return True
        else:
            print(f'The {ope} element in the doubly lined list is ', self.tail.value)
            addr = self.tail
            self.tail = self.tail.prev
            addr = self.tail.next = None
            if(ope != 'poped'):
                return True
        self.length -= 1
    
    def prepend(self, value, ope = 'prepended'):
        new_node = Node(value)
        if(not self.head):
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(f'The {ope} value is ', new_node.value)
        if(ope != 'prepended'):
            return True
        self.length += 1
    
    def pop_first(self, ope = 'first poped'):
        if(not self.head):
            print('Their are no elements in doubly linked list to run pop_first function')
            return False
        elif(self.length == 1):
            print(f'The {ope} element is ', self.head.value)
            self.tail = self.head = None
            if(ope != 'first poped'):
                return True
        else:
            print(f'The {ope} element is ', self.head.value)
            addr = self.head
            self.head = self.head.next
            addr.next = self.head.prev = None
            if(ope != 'first poped'):
                return True
        self.length -= 1
    
    def get(self, index):
        if(not self.head):
            print('Their are no elements in the doubly linked list to get')
            return False
        elif(index < 0 or index >= self.length):
            print(f'Give the index between 0 and {self.length} to get')
            return False
        if(index < (self.length) // 2):
            curr = self.head
            for i in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.length - 1, index, -1):
                curr = curr.prev
        print(f'The element at index {index} is ', curr.value)
    
    def set(self, index, value):
        if(not self.head):
            print('Their are no elements in the doubly linked list to set')
            return False
        elif(index < 0 or index >= self.length):
            print(f'Give the index between 0 and {self.length} to set')
            return False
        if(index < (self.length) // 2):
            curr = self.head
            for i in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.length - 1, index, -1):
                curr = curr.prev
        curr.value = value
        print(f'The element {value} is setted at index {index}')
    
    def insert(self, index, value):
        if(index < 0 or index >= self.length):
            print(f'Give the index between 0 and {self.length} to insert')
            return False
        elif(index == 0):
            self.prepend(value, 'inserted')
        else:
            new_node = Node(value)
            if(index < (self.length) // 2):
                curr = self.head
                for i in range(index):
                    curr = curr.next
            else:
                curr = self.tail
                for i in range(self.length - 1, index, -1):
                    curr = curr.prev
            new_node.next = curr
            curr.prev.next = new_node
            new_node.prev = curr.prev
            curr.prev = new_node
            print('The inserted value is ', value)
        self.length += 1
    
    def remove(self, index):
        if(not self.head):
            print('Their are no elements in the doubly linked list to remove')
            return False
        elif(index < 0 or index >= self.length):
            print(f'Give the index between 0 and {self.length} to remove')
            return False
        else:
            if(index == 0):
                self.pop_first('removed')
            elif(index == (self.length) - 1):
                self.pop('removed')
            else:
                if(index < (self.length) // 2):
                    curr = self.head
                    for i in range(index):
                        curr = curr.next
                else:
                    curr = self.tail
                    for i in range(self.length - 1, index, -1):
                        curr = curr.prev
                print('The removed element is ', curr.value)
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next = curr.prev = None
            self.length -= 1
    
    def reverse(self):
        if(not self.head):
           print('Their are no elements to reverse in the doubly linked list')
           return False
        else:
            curr = self.head
            while(curr):
                curr.prev, curr.next = curr.next, curr.prev
                curr = curr.prev
            self.tail, self.head = self.head, self.tail
    
    def palindrome(self):
        if(not self.head):
           print('Their are no elements to reverse in the doubly linked list')
           return False
        else:
            curr_tail, curr_head = self.tail, self.head
            while((curr_head != curr_tail) and (curr_head.prev != curr_tail)):
                if(curr_head.value != curr_tail.value):
                    print('The doubly linked list is not a palindrome')
                    return False
                else:
                    curr_tail, curr_head = curr_tail.prev, curr_head.next
            print('The given doubly linked list is a palindrome')
            return True
    
    def swap_nodes_in_pairs(self):
        curr = self.head
        while(curr and curr.next):
            curr.next.value, curr.value = curr.value, curr.next.value
            curr = curr.next.next



dll = DoublyLinkedList(10)
dll.append(20)
dll.append(30)
dll.print_list()
dll.pop()
dll.make_empty()
dll.print_list()
dll.prepend(20)
dll.print_list()
dll.pop_first()
dll.print_list()
dll.append(20)
dll.prepend(30)
dll.prepend(40)
dll.print_list()
dll.get(2)
dll.set(0, 5)
dll.set(8, 2000)
dll.print_list()
dll.insert(4, 75)
dll.print_list()
dll.remove(2)
dll.print_list()
dll.insert(3, 1)
dll.print_list()
dll.remove(2)
dll.print_list()
print('After swapping the pair of nodes : ')
dll.swap_nodes_in_pairs()
dll.print_list()
print('Reversing the elements in the doubly linked list : ')
dll.reverse()
dll.print_list()
dll.palindrome()