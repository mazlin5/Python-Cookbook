# key value pair using hash function to store items into index
# one-way - deterministic (particualar hash func we expect a certain output index)
# create link (address) - key:value pair
# 
# collions - assign key:value pair to address with an item already
#  open addressing - seperate chaining 
#  linked-list at addresses then iterate through to find specific items 

# always have prime # for addresses
# subtract len(array) - 1 so prime # increase randomness to reduce collisions 

class HashTable:
    def __init__(self, size = 7):
        # create list called data_map of 7 empty elements
        self.data_map = [None] * size

    # 
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # gets askie number for alphanumeric
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # SET key:value pair in hash table
    def set_item(self, key, value):
        # figure out address for key:val pair
        index = self.__hash(key)

        # initialize empty list at address
        # only do this if empty list has not been created
        if self.data_map[index] == None:
            self.data_map[index] = []
        
        # take key:val and insert into empty list
        self.data_map[index].append([key, value])


    # get items from hash table
    def get_item(self, key):
        
        # find address/index of key by passing to __hash()
        index = self.__hash(key)
        # take that index value and use o(1) to get item from self.data_map[index]

        # if self.data_map[index] == None then fail 
        if self.data_map[index] is not None:

            # loop linked-lists in list at index
            for i in range(len(self.data_map[index])):

                # loop keys for match of keys
                # i = iteration above = 0 then first item in that linked list
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i]
        return None

    # take all keys and put them into a list and return
    def keys(self):
        # create empty list
        all_keys = []

        # loop through main hash table
        for i in range(len(self.data_map)):
            # ensure there is data 
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

my_hash_table  = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('stolb', 1500)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.set_item('umberl', 80)
# print(my_hash_table.get_item('bolts'))

# print(my_hash_table.keys())
my_hash_table.print_table()