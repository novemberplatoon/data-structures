class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack

  def __init__(self):
    self.total = 0
    self.stack = []

  def push(self, elem):
    # write your code to add data following LIFO and return the Stack
    self.stack.append(elem)
    self.total += 1
    return self.stack

  def pop(self, data):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.pop()
    self.total -= 1
    return self.stack

  def size(self):
    # write your code that returns the size of the Stack
    return self.total


s = Stack()
s.push(2)
s.pop(1)
s.push(2)
print(s.size())
