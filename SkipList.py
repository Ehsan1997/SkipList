# SkipList Class and SkipListNode Class
# SkipListNode is a special node made for SkipList as each node represents a list on a level \
#  in the skiplist

# Imports
# Need random number for coin toss
from random import randint
# Need Sorted Linked List
from SortedLinkList import SortedLinkList

class SkipListNode:
  # ll is for Link List
  def __init__(self):
    self.next_level = None
    self.ll = SortedLinkList()


class SkipList:
  def __init__(self):
    # Level 1
    self.l1 = SkipListNode()
    # Highest Level
    self.max_level = self.l1


  # Number of Levels
  def count_list(self):
    n = 0
    l = self.l1
    while l.next_level:
      n+=1
      l = l.next_level
    return n

  def insert(self, value):
    # Insert in the first level link list
    down_node = self.l1.ll.insert(value)
    # Coin toss
    current_level = self.l1
    while randint(0,1) == 0:
      if current_level.next_level:
        current_level = current_level.next_level
        node = current_level.ll.insert(value)
      else:
        current_level.next_level = SkipListNode()
        current_level = current_level.next_level
        node = current_level.ll.insert(value)
      node.down = down_node
      down_node = node
      self.max_level = current_level

  def print_list(self):
    i = 1
    l = self.l1
    while l:
      print(f"l{i}:")
      l.ll.print_list()
      l = l.next_level
      i+=1

  def elem_count_each_level(self):
    # A list containing count of elements on each level.
    elem_count = []
    current_list = self.l1
    while current_list:
      elem_count.append(current_list.ll.count())
      current_list = current_list.next_level
    return elem_count
  
  # Search for existence of an element
  # 0 if not found and 1 if found
  def search(self, value):
    # Number of hops
    hops = 0
    current_node = self.max_level.ll.start_node.next
    while current_node.value != value and current_node.down:
      hops+=1
      if current_node.next:
        if current_node.next.value > value:
          current_node = current_node.down
        else:
          current_node = current_node.next
      else:
        current_node = current_node.down

    # If current_node value is equal to value
    if current_node.value == value:
      return 1, hops
    else:
      # If current node has greater value go to left
      if current_node.value > value:
        while current_node.value > value and current_node.prev:
          hops+=1
          current_node = current_node.prev
          # If we get a none, we are done here.
          if current_node is None: break
      # If current node is less in value, go to right
      else:
        while current_node.value < value and current_node.next:
          hops+=1
          current_node = current_node.next
          # If we get a none, we are done here.
          if current_node is None: break

    return 1 if current_node.value == value else 0, hops