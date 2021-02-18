class Queue:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
    def __init__(self):
        self.store = []

    def enqueue(self, element):
        # write your code to add data to the Queue following FIFO and return the Queue
        self.store.insert(0, element)
        return self.store

    def dequeue(self, data):
        # write your code to removes the data to the Queue following FIFO and return the Queue
        self.store.pop()
        return self.store

    def size(self):
        # write your code that returns the size of the Queue
        return len(self.store)


q = Queue()
q.enqueue(1)
q.enqueue(10)
q.enqueue(100)
q.enqueue(1000)
print(q.size())
