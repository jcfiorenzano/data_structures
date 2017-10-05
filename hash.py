import sys

class ChainingHashTable:

    def __init__(self, hashStrategy):
        self._hash_strategy = hashStrategy
        self._hash_table = [None] * hashStrategy.optimusSize()

    def insert(self, item):
        key = self._hash_strategy.hash(item)

        if(self._hash_table[key] == None):
            self._hash_table[key] = []
        
        self._hash_strategy[key].append(item)

    def search(self, item):
        key = self._hash_strategy.hash(item)

        return item in self._hash_table[key]

    def remove(self, item):
        key = self._hash_strategy.hash(item)

        if(item in self._hash_table[key]):
            self._hash_table.remove(item)
            


class DivisionMethodStrategy:
    
    def optimusSize(self):
        return 65537

    def hash(self, k):
        return k % self.optimusSize()

class MultiplicationMethodStrategy:
    def optimusSize(self):
        return 65536

    def hash(self, k):
        a = 0.6180339
        w = sys.getsizeof(int)
        r = 16
        return ( (a * k) % 2^w) >> (w - r)

def main():
    table = ChainingHashTable(DivisionMethodStrategy())


if __name__ == '__main__':
    main()
    
    
