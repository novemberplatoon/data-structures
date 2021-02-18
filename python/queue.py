# NOTE: I followed the instructions as given in the comments for this code. However, this is not the ideal way to program
#  a Queue (dequeue should return the element dequeued and not the queue itself, etc.). I can redo it if need be!

class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self, queue=[]):
    self.total = len(queue)
    self.queue = queue

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.insert(0, data)
    self.total += 1
    return self.queue

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    self.queue.pop()
    self.total -= 1
    return self.queue

  def size(self):
    # write your code that returns the size of the Queue
    return self.total
