class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self):
    self.head = None
    self.length = 0

  def add(self, data):
    # write your code to ADD an element to the Linked List
    new_node = Node(data)
    old_node = self.head
    self.head = new_node
    self.head.next = old_node

    self.length += 1


  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    if self.head is None: 
      return False
    if self.head == data:
      head = self.head.next
    else:
      current = self.head
      while current.next:
        if current.next.data == data:
          current.next = current.next.next
          self.length -= 1
          return current.next
        current = current.next


  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    if self.head is None: 
      return False
    else:
      current = self.head
      if current.data == element_to_get:
        return current.data
      while current.next:
        current = current.next
        if current.data == element_to_get:
          return current.data
      return False

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, data):
    self.data = data
    self.next = None


test = LinkList()
test.add(1)
test.add(2)
test.add(3)
print(test.length)
 
test.remove(1)
print(test.length)
