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


  def count(self):
    n = 0
    node = self.start_node
    while node.next:
      node = node.next
      n+=1
    return n
    
  def insert(self, value):
    # Initial (Empty list) Case
    if self.count() == 0:
      self.start_node.next = Node(value, prev=self.start_node)
      return self.start_node.next
    # Start with the current node
    node = self.start_node
    # Check the next node (A minute optimization)
    node_next = node.next
    # If the next Node is not None, then insert in sorted way
    while node_next.value < value:
      node = node_next
      node_next = node_next.next
      if node_next == None: break
    # Means insertion is not at the end of the list
    if node_next:
      new_node = Node(value, node_next, prev=node)
      node.next = new_node
      return new_node
    # Insertion to the end of the list
    else:
      node.next = Node(value, prev=node)
      return node.next
    # Return new node, so down pointer can be assigned

  def linear_search(self, value):
    hops = 0
    node = self.start_node
    while node.next:
      hops+=1
      if node.value == value:
        return 1, hops
      elif node.next.value > value:
        return 0, hops
      node = node.next
    return 1 if node.value == value else 0, hops