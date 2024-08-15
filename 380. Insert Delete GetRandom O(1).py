import random

class RandomizedSet:

    def __init__(self):
        self.rset = set()
        
    def insert(self, val: int) -> bool:
        before_length = len(self.rset)
        self.rset.add(val)
        if len(self.rset)==before_length:
            return False
        return True

    def remove(self, val: int) -> bool:
        try:
            self.rset.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        length = len(self.rset)
        if not length:
            return 
        index = random.randint(0,length-1)
        return list(self.rset)[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()