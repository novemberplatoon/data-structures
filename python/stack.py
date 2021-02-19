class Stack:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
    def __init__(self):
        self.num_elements = 0
        self.storage = []

    def push(self, data):
        # write your code to add data following LIFO and return the Stack
        self.storage.append(data)
        self.num_elements += 1

    def pop(self):
        # write your code to removes the data following LIFO and return the Stack
        popped_item = self.storage.pop()
        self.num_elements -= 1
        return popped_item

    def size(self):
        # write your code that returns the size of the Stack
        return self.num_elements

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.storage)
# s.pop()
# print(s.storage)
# print(s.size())