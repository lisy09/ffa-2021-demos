import numpy as np

class SumTree:
    write = 0

    def __init__(self, capacity:int) -> None:
        self.capacity = capacity
        self.tree = np.zeros(2*capacity - 1)
        self.data = np.zeros(capacity, dtype=object)
        self.n_entries = 0

    def _propagate(
        self,
        idx:int,
        change,
    ):
        """
        update to the root node
        """
        parent = (idx-1)//2
        self.tree[parent] += change
        if parent != 0:
            self._propagate(parent, change)

    def _retrieve(self, idx:int, s):
        """
        find sample on leaf node
        """
        left = 2*idx+1
        right = left +1

        if left >= len(self.tree):
            return idx
        
        if s<= self.tree[left]:
            return self._retrieve(left, s)
        else:
            return self._retrieve(right, s-self.tree[left])

    def total(self):
        return self.tree[0]
    
    def update(self, idx:int, p):
        """
        update priority
        """
        change = p - self.tree[idx]
        self.tree[idx] = p
        self._propagate(idx, change)
    
    def add(self, p, data):
        """
        store priority and sample
        """
        idx = self.write + self.capacity - 1

        self.data[self.write] = data
        self.update(idx, p)

        self.write += 1
        if self.write >= self.capacity:
            self.write = 0
        
        if self.n_entries < self.capacity:
            self.n_entries += 1
    
    def get(self, s):
        idx = self._retrieve(0, s)
        dataIdx = idx - self.capacity + 1
        return (idx, self.tree[idx], self.data[dataIdx])