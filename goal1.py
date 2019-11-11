# Import skiplist
from SkipList import SkipList
from random import randint
import time
import csv

sl = SkipList()
# sl = SortedLinkList()
arr = [10, 3, 7, 2, 91, 1]
for a in arr:
  sl.insert(a)
sl.print_list()


sl = SkipList()
list_csv = []
for i in range(100):
  k = randint(0, 100000)
  print(f'Inserting: {k}')
  sl.insert(k)
  list_csv.append(sl.elem_count_each_level())

level_count = sl.count_list()
for l in list_csv:
  diff = level_count - len(l)
  for i in range(diff):
    l.append(0)

with open('out.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerows(list_csv)


print ("Done inserting!!")

# sl.print_list()
start = time.time()
print(f"Status: {sl.search(k+1)}")
end = time.time()
print(f'Time1: {end - start}')

start = time.time()
print(f"Status: {sl.l1.ll.linear_search(k+1)}")
end = time.time()
print(f'Time2: {end - start}')
