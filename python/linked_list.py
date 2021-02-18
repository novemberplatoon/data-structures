class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self):
        self.length = 0
        self.head = Node(None)

    def add(self, data):
        # write your code to ADD an element to the Linked List
        new_node = Node(data)
        temp_ref = self.head
        while temp_ref.next:
            temp_ref = temp_ref.next
        temp_ref.next = new_node
        self.length += 1

    # Works except for last Node (bug)
    def remove(self, data):
        # write your code to REMOVE an element from the Linked List
        temp_before = self.head
        curr_node = self.head
        while curr_node.next:
            temp_next = curr_node.next
            if data == curr_node.data:
                temp_before.next = temp_next
                del curr_node
                self.length -= 1
                return
            else:
                temp_before = curr_node
            curr_node = curr_node.next
        # Probably not the best way
        # First Node edge case
        if self.head.next.data == data:
            temp_node = self.head.next
            self.head.next = self.head.next.next
            self.length -= 1
            del(temp_node)

    def get(self, element_to_get):
        # write you code to GET and return an element from the Linked List
        pass

    def print_nodes(self):
        curr_in = 0
        curr_node = self.head.next
        while curr_in < self.length:
            print(f"index: {curr_in} data: {curr_node.data}")
            curr_in += 1
            curr_node = curr_node.next
# ----- Node ------


class Node:
    # store your DATA and NEXT values here
    def __init__(self, data):
        self.data = data
        self.next = None


test_link = LinkList()
test_link.add(5)
test_link.add(7)
test_link.add(3)
test_link.add(1)
test_link.remove(5)
test_link.remove(1)
test_link.print_nodes()
