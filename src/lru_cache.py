class LRU_cache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end to show that it was recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end
            self.order.remove(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used item
                lru_key = self.order.pop(0)
                del self.cache[lru_key]

        # Add the new key-value pair
        self.cache[key] = value
        self.order.append(key)
            

        
# Example usage:
lru = LRU_cache(2)
lru.put(1, 1)     # cache is {1=1}
lru.put(2, 2)     # cache is {1=1, 2=2}
print(lru.get(1)) # return 1
lru.put(3, 3)     # evicts key 2, cache is {1=1, 3=3}
print(lru.get(2)) # returns -1 (not found)
lru.put(4, 4)     # evicts key 1, cache is {4=4, 3=3}
print(lru.get(1)) # returns -1 (not found)
print(lru.get(4)) # returns 4

# This is a simple implementation of an LRU (Least Recently Used) cache.
# It supports get and put operations in O(1) time complexity.
# The cache has a fixed capacity, and when it exceeds this capacity,
# it evicts the least recently used item.
# The order of usage is tracked using a list.
# The order of usage is tracked using a list.
# Note: This implementation can be further optimized using OrderedDict from collections module.

