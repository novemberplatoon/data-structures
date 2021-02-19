class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self, head = None):
        self.head = head
        self.length = 0

    def prepend(self, data):
    # write your code to ADD an element to the Linked List
        new_head = Node(data)
        old_head = self.head
        self.head = new_head
        self.head.next = old_head

        self.length += 1

    def remove(self, target_value):
    # write your code to REMOVE an element from the Linked List
        temp = self.head
        if temp.data == target_value: # first element is target data
            self.head = temp.next
            return
        while temp.next:
            prev = temp
            temp = temp.next
            if temp.data == target_value:
                prev.next = temp.next

        self.length -= 1

    def get(self, index_to_get):
    # write you code to GET and return an element from the Linked List
        count = 0 
        if index_to_get == count:
            return self.head.data
        else: 
            while self.head.next: 
                self.head = self.head.next
                count += 1
                if index_to_get == count:
                    return self.head.data


    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# ----- Node ------
class Node:
    # store your DATA and NEXT values here
    def __init__(self, data):
        self.data = data
        self.next = None

ll = LinkList()
ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
ll.prepend(4)

ll.print_list()
print('\n')
ll.remove(2)
ll.print_list()

ll.prepend(5)
ll.prepend(6)
ll.print_list()
print('\nGet value at index 2: ')
print(ll.get(2))