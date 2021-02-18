class Stack:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
    def __init__(self):
        self.storage = []

    def push(self, data):
        # write your code to add data following LIFO and return the Stack
        self.storage.append(data)

    def pop(self, data):
        # write your code to removes the data following LIFO and return the Stack
        if len(self.storage) == 0:
            return -1
        self.storage.pop()

    def size(self):
        # write your code that returns the size of the Stack
        return len(self.storage)


test_list = []
print(test_list.pop())
