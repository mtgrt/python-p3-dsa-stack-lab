class Stack:
    def __init__(self, items=None, capacity=None):
        self.items = items if items is not None else []
        self.capacity = capacity

    def push(self, item):
        if self.capacity is None or len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return self.capacity is not None and len(self.items) >= self.capacity

    def search(self, item):
        try:
            return len(self.items) - self.items[::-1].index(item)
        except ValueError:
            return None
