class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.element_total = 0
    self.element_queue = []

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.element_queue.insert(0, data)
    self.element_total += 1

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    self.element_queue.pop()
    self.element_total -= 1

  def size(self):
    # write your code that returns the size of the Queue
    return self.element_total

test = Queue()

test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
print(test.element_queue)
print(test.element_total)
test.dequeue()
print(test.element_queue)
print(test.element_total)