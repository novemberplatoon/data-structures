class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self):
        self.head = None

    def add(self, data):
        # write your code to ADD an element to the Linked List
        new_node = Node(data)
        old_node = self.head
        self.head = new_node
        self.head.next = old_node

    def remove(self, data):
        # write your code to REMOVE an element from the Linked List
        if self.head is None:
            return False
        else:
            current = self.head
            print("Currently checking head " + str(current))
            if current.data == data:
                print("Removing " + str(current))
                self.head = current.next
                current = None
                return
            while current.next:
                print("Current data is " + str(current.data))
                previous = current
                current = current.next
                print("Moving to next " + str(current))

                if current.data == data:
                    print("Removing " + str(current))

                    previous.next = current.next
                    break

    def get(self, element_to_get):
        # write you code to GET and return an element from the Linked List
        if self.head is None:
            return False
        else:
            current = self.head
            count = 0

            while current.next:
                if(count == element_to_get):
                    print("Got element " + str(current.data))
                    return current.data
                count += 1
                current = current.next

    def printList(self):
        current = self.head
        while(current):
            print(" %d" % (current.data))
            current = current.next

# ----- Node ------


class Node:
    # store your DATA and NEXT values here
    def __init__(self, data):
        self.data = data
        self.next = None


link_list = LinkList()

link_list.add(11)
link_list.add(24)
link_list.add(36)
link_list.add(45)
link_list.add(57)
link_list.add(75)


link_list.printList()
link_list.get(2)
link_list.remove(4)
link_list.printList()
