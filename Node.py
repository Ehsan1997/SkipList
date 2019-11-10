# A somewhat special node as it is designed for use in skip list, in addition to having two pointers \
# it has three (next, previous and down).

# This class is used by SortedLinkList, but is somewhat different to a regular link list node.

class Node:
  def __init__(self, value, next=None, prev=None, down=None,):
    self.value = value
    self.next = next
    self.down = down
    self.prev = prev