# Import skiplist
from SkipList import SkipList
from random import randint
import time

sl = SkipList()
# sl = SortedLinkList()
arr = [10, 3, 7, 2, 91, 1]
for a in arr:
  sl.insert(a)
sl.print_list()
sl = SkipList()
for i in range(10000):
  k = randint(0, 100000)
  print(f'Inserting: {k}')
  sl.insert(k)

print ("Done inserting!!")

# sl.print_list()
start = time.time()
print(f"Status: {sl.search(k)}")
end = time.time()
print(f'Time1: {end - start}')

start = time.time()
print(f"Status: {sl.l1.ll.linear_search(k)}")
end = time.time()
print(f'Time2: {end - start}')
