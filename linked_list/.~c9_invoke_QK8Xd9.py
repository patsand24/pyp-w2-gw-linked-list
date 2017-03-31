from .interface import AbstractLinkedList
from .node import *


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        if elements is not None:
            for elem in elements:
                self.append(elem)
        
    def __str__(self):
        str_list = []
        for i in iter(self):
            str_list.append(i.elem)
        return str(str_list)

        
    def __len__(self):
        total = 0
        for item in iter(self):
            total += 1
        return total


    # martins generator code
    #   def _range(start, end, step = 0):
    #       current = start
    #       while current < end:
    #           num = current
    #           current += 1
    #           yield num
    #   gen = _range (0,4) 
    #   print(gen) 
    def __iter__(self):
        current = self.start
        while current is not None:
            yield current
            current = current.next
        raise StopIteration
        

    def __getitem__(self, index):
        for i, elem in enumerate(iter(self)):
            if i == index:
                return elem
        raise IndexError

    def __add__(self, other):
        new_list = self.__class__([elem for elem in self])
        for elem in other:
            new_list.append(elem.elem)
        return new_list
        
        
    
    def __iadd__(self, other):
        #return self.__add__(self, other)
        if self.start == None:
            self.start = other.start
            self.end = other.end
        elif other.start == None:
            pass
        else:
            self.end.next = other.start
            self.end = other.end
        return self
    
    
    def __ne__(self, other):
        self_elem = self.start
        other_elem = other.start
        
        if not self_elem or not self_elem.next:
            return self_elem != other_elem
        while self_elem.next:
            if self_elem != other_elem:
                return True
            self_elem = self_elem.next
            other_elem = other_elem.next
        return False
    
        
    def __eq__(self, other):
        '''
        self_elem = self.start
        other_elem = other.start
    
        if not self_elem or not self_elem.next:
            return self_elem == other_elem
        while self_elem.next:
            if self_elem.elem != other_elem.elem:
                return False
            self_elem = self_elem.next
            other_elem = other_elem.next
        return True
        '''
         
        self_list = [each for each in enumerate(self)]
        other_list = [each for each in enumerate(other)]
        if self_list == other_list:
            return True
            
            
    def append(self, elem):
        new_node = Node(elem)
        if not self.start:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node


    def count(self):
        counter = 0
        '''a = self.iter()
        for link in a:
            count += 1
        return count
        '''
        a = self.start
        while a is not None:
            counter += 1
            a = a.next
        return counter


    def pop(self, index=None):
        

        if index > self.count()-1 or self.count() == 0:
            raise IndexError
        
        if index == 1 or self.count() == 1:
            if self.count() == 1:
                val = self.start
                self.start = None
                self.end = None
                return val.elem
            else:
                val = self.start
                self.start = val.next
                return val.elem
        
        if index == None or index == self.count()-1:
            # pop last element
            gen = iter(self)
            previous_link = self.start
            for link in gen:
                if link.next is None:
                    previous_link.next = None
                    self.end = previous_link
                    return link.elem
                previous_link = link
            
        else:
            # all other cases
            gen = iter(self)
            counter = 0
            previous_link = self.start
            for link in gen:
                if counter == index:
                    previous_link.next = link.next
                    return link.next
                previous_link = link
                
        
        ''''''
        
       
        
        # def test_pop_removes_last_item(self):
        
        # def test_pop_removes_last_item_by_default(self):
        def pop(self, index=None):
            if (self.count() == 0) or (self.count()-1 < index): 
                # def test_pop_raises_an_exception_with_empty_list(self):
                raise IndexError
            elif self.count() == 1:
                # def test_pop_with_a_single_element_list(self):
                if index > 0:
                    raise IndexError
                else:
                    # clear list
                    previous_node = self.start
                    self.start = None 
                    self.end = None
                    return previous_node.elem
            elif index == 0: 
                # def test_pop_removes_first_item(self):
                previous_node = self.start
                self.start = self.next
                return previous_node.elem
            elif index < self.count()-1:
                # def test_pop_removes_item_in_the_middle_of_the_list(self):
                gen = __iter__()
                count
                previous_node = self.start
                for node in gen:
                    if count == index:
                        # we found the Node we are looking for!
                        previous_node.next = node.next
                        r
                        
                
       
            