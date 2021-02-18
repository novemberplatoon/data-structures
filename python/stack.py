class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.element_total = 0
    self.element_stack = []

  def push(self, element):
    # write your code to add data following LIFO and return the Stack
    self.element_stack.append(element)
    self.element_total += 1

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.element_stack.pop()
    self.element_total -= 1

  def size(self):
    # write your code that returns the size of the Stack
    return self.element_total


test = Stack()

print(test.size())
test.push(1)
test.push(2)
print(test.element_stack)
print(test.size())
test.pop()
print(test.element_stack)
print(test.size())