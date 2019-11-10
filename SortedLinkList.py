# Python doesn't provide it's own representation of LinkList, further we required a special type of \
# Link list, where the values were inserted in a sorted order

# Import Node class, see Node.py for details
from Node import Node

class SortedLinkList:
  def __init__(self):
    self.start_node = Node(None, prev=None)
    
  def print_list(self):
    node = self.start_node.next
    while node:
      if(node.next):
        print(node.value, end=", ")
      else:
        print(node.value)
      node = node.next
  # Python won't allow def(self, self.start_node, n = 0)
  def count(self):
    def count(node=self.start_node, n=0):
      if node.next == None:
        return n
      else:
        return count(node.next, n + 1)
    # This is calling the inner count method
    return count()
    
  def insert(self, value):
    node = self.start_node
    # Empty List
    if node.next is None:
      new_node = Node(value, None, node)
      node.next = new_node
      return new_node
    # Iterate till the end or where the next element is larger/
    while node.next.value < value:
      node = node.next
      # End of the list, just append the value and return
      if node.next is None:
        new_node = Node(value, None, node)
        node.next = new_node
        return new_node
    # Final case if next value is greater than the new value
    new_node = Node(value, node.next, node)
    node.next = new_node
    node.next.prev = new_node
    return new_node