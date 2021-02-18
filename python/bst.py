class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # This is where you will insert a value into the Binary Search Tree
        if not self.root:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
    # Private helper function that's recursive

    def _insert(self, value, current_node):
        # Edge case: if value is already in the tree
        if value == current_node.value:
            print("This value is already in the BST!")
            return

        # If value we're about to insert is less than the node we're on...
        if value < current_node.value:
            # If current node does not have a left child, create a new node and insert it as the left child
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                # If the current node does have a left child, then we recurse and pass in the value and current node that we're on
                self._insert(value, current_node.left)
        # Same as the left subtree, but now we're applying it to the right subtree
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)

    def contains(self, value):
        # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST

        # In order traversal
        self.in_order_array = self.in_order_traversal(self.root)
        if value in self.in_order_array:
            return True
        else:
            return False

    def in_order_traversal(self, current_node):
        elements = []
        # If the current node does not equal None
        if current_node:
            # visit left subtree
            elements += self.in_order_traversal(current_node.left)

            elements.append(current_node.value)

            elements += self.in_order_traversal(current_node.right)

        return elements

    def remove(self, value):
        # this is where you will remove a value from the BST
        pass


# ----- Node ------
class Node:
    # store your DATA and LEFT and RIGHT values here
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


b = Bst()

b.insert(8)
b.insert(3)
b.insert(1)
b.insert(6)
b.insert(4)
b.insert(7)
b.insert(10)
b.insert(14)
b.insert(13)

print(b.contains(1))
