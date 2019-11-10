# A somewhat special node as it is designed for use in skip list, in addition to having two pointers \
# it has three (next, previous and down).

# This class is used by SortedLinkList and SkipList both, that is why placed in a separate file.

class Node:
  def __init__(self, value, next=None, down=None, prev=None):
    self.value = value
    self.next = next
    self.down = down
    self.prev = prev