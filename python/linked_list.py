class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head=None):
    self.head = head
    self.length = 0

  def add(self, data):
    # write your code to ADD an element to the Linked List
    if self.head == None:
      self.head = Node(data)
      self.length += 1
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = Node(data)
      self.length += 1
    pass

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    temp = self.head
    if temp.data == data:
      self.head = temp.next
    else:
      while temp.next != None:
        if temp.next.data == data:
          #Remove the required node from the list
          temp.next = temp.next.next
          break
        else:
          temp = temp.next
    pass

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    counter = 0
    temp = self.head
    while counter != element_to_get:
      temp = temp.next
      counter += 1
    return temp

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, data):
    self.data = data
    self.next = None

