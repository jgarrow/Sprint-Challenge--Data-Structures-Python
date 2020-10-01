class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        self.oldest = 0 # keep track of index of oldest item in store

    def append(self, item):
        # if there's still room, add item
        if len(self.store) < self.capacity:
            self.store.append(item)
        else:
            # insert new item at current index of oldest item
            # then pop off oldest item (whose new index is oldest + 1)
            self.store.insert(self.oldest, item)
            self.store.pop(self.oldest + 1)
            
            # update self.oldest
            if self.oldest + 1 < self.capacity:
                self.oldest += 1
            else:
                self.oldest = 0

    def get(self):
        return self.store