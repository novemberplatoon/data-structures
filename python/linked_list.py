class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self):
        self.head = None

    def add(self, data):
        # write your code to ADD an element to the Linked List
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            old_node = self.head
            self.head = new_node
            self.head.next_node = old_node

    def remove(self, target):
        # write your code to REMOVE an element from the Linked List
        previous = None
        current = self.head
        if self.head is None:
            return False
        else:
            while current:
                if current.data == target:
                    if previous:
                        previous.next_node = current.next_node
                    else:
                        self.head = current.next_node
                previous = current
                current = current.next_node
            return False

    def get(self, target):
        if self.head is None:
            return False
        else:
            current = self.head
            if current.data == target:
                return True
            while current.next_node:
                current = current.next_node
                if current.data == target:
                    return True
            return False

    def print_list(self):
        this_node = self.head
        while this_node is not None:
            print(this_node, end="->")
            this_node = this_node.next_node
        print('None')
# ----- Node ------


class Node:
    # store your DATA and NEXT values here
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

    def __str__(self):
        return ('(' + str(self.data) + ')')
