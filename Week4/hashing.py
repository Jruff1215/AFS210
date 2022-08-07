class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        return key % self.size
    
    def rehash(self,key):
        # Insert your secondary hashing function code
        return key // self.size
    
    def put(self,key,data):
        # Insert your code here to store key and data 
        hashValue = self.hashfunction(key)
        if self.data[hashValue] is None:
           self.data[hashValue] = data
           self.slots[hashValue] = key
        else:
            if(self.slots[hashValue] == key):
                self.data[hashValue] = data
            else:
                hashValue = self.rehash(key)
                if self.data[hashValue] is None:
                    self.data[hashValue] = data
                    self.slots[hashValue] = key
                else:
                    return None
 


    def get(self,key):
        # Insert your code here to get data by key
        hashValue = self.hashfunction(key)
        while self.slots[hashValue] is not None:
            if self.slots[hashValue] is key:
                return self.data[hashValue]

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
# Store remaining input data
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values

# print the data values

# print the value for key 52
print(H.slots)
print(H.data)
print(H[52])