class Stack:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
    def __init__(self):
        self.stack = []

    def push(self, item):
        # write your code to add data following LIFO and return the Stack
        self.stack.append(item)

    def pop(self):
        # write your code to removes the data following LIFO and return the Stack
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print("Your stack is empty!")
            return "Your stack is empty!"

    def size(self):
        # write your code that returns the size of the Stack
        print(len(self.stack))
        return len(self.stack)
