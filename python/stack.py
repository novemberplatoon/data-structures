# NOTE: I followed the instructions as given in the comments for this code. However, this is not the ideal way to program
#  a Stack (pop should return the element popped and not the stack itself, etc.). I can redo it if need be!

class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self, stack=[]):
    self.total = len(stack)
    self.stack = stack

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack.append(data)
    self.total += 1
    return self.stack

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.pop()
    self.total -= 1
    return self.stack

  def size(self):
    # write your code that returns the size of the Stack
    return self.total

