# Import skiplist
from SkipList import SkipList
from SortedLinkList import SortedLinkList
from random import randint

sl = SkipList()
# sl = SortedLinkList()
# arr = [10, 3, 7, 2, 91, 1]
for i in range(10):
  sl.insert(randint(0, 1000000))
sl.print_list()
print(f"Status: {sl.search(10)}")