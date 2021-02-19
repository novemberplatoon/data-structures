class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.total = 0
    self.queue = []

  def enqueue(self, elem):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.insert(0, elem)
    self.total += 1

  def dequeue(self, data):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    self.queue.pop()
    self.total -= 1

  def size(self):
    # write your code that returns the size of the Queue
    return self.total

q = Queue()
q.enqueue(5)
q.enqueue(9)
q.enqueue(7)
q.dequeue(5)
print(q.size())