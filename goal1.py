# Import skiplist
from SkipList import SkipList

sl = SkipList()
# sl = SortedLinkList()
arr = [10, 3, 7, 2, 91, 1]
for a in arr:
  sl.insert(a)
sl.print_list()

print(f"Status: {sl.search(10)}")