class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        return sum(ord(car) for car in string)

    def add(self, key, val):
        hashed = self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed] = {}
        self.collection[hashed][key] = val
         

    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
           del self.collection[hashed][key]

    def lookup(self, key):
        hashed = self.hash(key)
        if hashed not in self.collection or key not in self.collection[hashed]:
            return None
        return self.collection[hashed][key]

