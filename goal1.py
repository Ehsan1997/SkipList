# Import skiplist
from SkipList import SkipList
from SortedLinkList import SortedLinkList
from random import randint

sl = SkipList()
# sl = SortedLinkList()
# arr = [10, 3, 7, 2, 91, 1]
for i in range(100):
  sl.insert(randint(0, 100000))
sl.print_list()
print(f"Status: {sl.search(10)}")