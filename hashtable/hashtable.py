from copy import copy

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}: {self.value}"
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def for_each(self, fn):
        fn(self.value)
        if self.next:
            self.next.for_each(fn)

class LinkedList:
    def __init__(self, key=None, value=None):
        node = HashTableEntry(key, value)
        self.size = 0
        self.head = node
        self.tail = node

    def __str__(self):
        list = []
        self.head.for_each(lambda x: list.append(x))        
        return " ".join(str(x) for x in list)

    def is_empty(self):
        return self.size == 0

    def add_to_head(self, key, value):
        new_node = HashTableEntry(key, value)

        if self.is_empty():
            self.head = new_node            
            self.tail = new_node
        else:
            # set new node to head
            new_node.set_next(self.head)
            #change head to new_node 
            self.head = new_node
        self.size += 1
        return value

    def add_to_tail(self, key, value):        
        # create the Node from the value 
        new_node = HashTableEntry(key, value)
  
        if self.is_empty():
           
            self.head = new_node
            self.tail = new_node        
        else:
            # tail already referring to a node? 
            self.tail.set_next(new_node)
            #reassign self.tail to refer to the new node
            self.tail = new_node
        self.size += 1

    def remove_head(self):
        # is there an empty LL?

        if self.is_empty():
            return
        # head and tail are pointing at the same Node 
        if not self.head.get_next():
            head = self.head 
            # delete the LLs head ref
            self.head = None
            # also delete the linked list's tail reference 
            self.tail = None 
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head 
        self.head = self.head.get_next()
        self.size -= 1
        return val

    def remove_tail(self):
        # if we have an empty linked list 
        if self.is_empty():
            return
        if self.tail == None:
            val = self.head.value
            self.remove_head()
            return val
        
        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()
        # store the value we're about to remove
        val = self.tail.get_value()
        # move self.tail to the Node right before
        if current == self.head:
            self.tail = None
        current.set_next(None)
        
        self.tail = current
        self.size -= 1
        return val
    
    def delete(self, key):
        if self.head.key == key:
            return self.remove_head()

        prev = self.head
        cur = self.head.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return cur.value
            #store the previous node for the next iteration
            prev = prev.next
            #set next for next iteratioin
            cur = cur.next
        
        return None     

    def contains(self, key):
        if not self.head:
            return None

        current = self.head
        
        while current:          
            if current.key == key:
                return current
            
            current = current.get_next()
        # no match
        return None

    def get_max(self):
        if not self.head:
            return 0
        
        # reference to the largest value 
        max_value = self.head.get_value()
        # reference to our current node 
        current = self.head.get_next()
        
        # check to see if we're still at a valid node        
        while current:
            if current.get_value() > max_value:
            	
                # if so, update our max_value variable
                max_value = current.get_value()            
                
            # update the current node to the next node in the list            
            current = current.get_next()
        #return max_value
        return max_value

    def __len__(self):
        return self.size

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, value=None):
        self.capacity = capacity
        ll = LinkedList()
        self.__hash_data = [copy(ll) for l in range(capacity)]
        print(self.__hash_data)

    def __str__(self):
        string = " ".join(l.head.value for l in self.__hash_data)
        return string


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.__hash_data)

    def total_items(self):
        count = 0
        for ll in self.__hash_data:
            count += len(ll)
        return count

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.total_items()/self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """
        FNV_prime = 1469511628211
        offset_basis = 1469581039346656037

        hash = offset_basis
        for char in key:
            hash = hash ^ ord(char)
            hash = hash * FNV_prime
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        pass


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """          
        if self.get_load_factor() < 0.2:
            pass
        elif self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)

        index = self.hash_index(key)
        node = self.__hash_data[index].contains(key)
        if node != None:
            node.value = value
        # if not, add to head
        else:
            self.__hash_data[index].add_to_head(key, value)
        return index


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # search ll at index
        index = self.hash_index(key)
        ll = self.__hash_data[index]
        # return value from deleted entry or None if it failed
        return ll.delete(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """        
        # .contains() returns None if not found
        node = self.__hash_data[self.hash_index(key)].contains(key)
        if node:
            return node.value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_capacity = self.capacity
        self.capacity = new_capacity

        additions = new_capacity - old_capacity
        ll = LinkedList()
        for _ in range(additions):
            self.__hash_data.append(copy(ll))
        
        hash_copy = copy(self.__hash_data)

        for ll in hash_copy:
            node = ll.head
            while node:
                key = node.key                
                if key != None:
                    new_index = self.hash_index(key)
                    #ll = LinkedList(node.key, node.value)
                    self.__hash_data[new_index] = ll
                node = node.next
    
    def get_hash_data(self):
        return self.__hash_data

if __name__ == "__main__":

    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    # # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
