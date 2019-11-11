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
n = 100
list_csv = []
list_to_search = []
for i in range(n):
  k = randint(0, 100000)
  print(f'Inserting: {k}')
  sl.insert(k)
  list_to_search.append(k)
  list_csv.append(sl.elem_count_each_level())

# Goal 1
level_count = sl.count_list()
for l in list_csv:
  diff = level_count - len(l)
  for i in range(diff):
    l.append(0)

list_csv.insert(0, [f'l{x+1}' for x in range(level_count)])

with open('out.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerows(list_csv)


print ("Done inserting!!")

# Goal 2

# sl.print_list()
start = time.time()
print(f"Status: {sl.search(k+1)}")
end = time.time()
print(f'Time1: {end - start}')

start = time.time()
print(f"Status: {sl.l1.ll.linear_search(k+1)}")
end = time.time()
print(f'Time2: {end - start}')

# List keeping track of values found
found = []
# List keeping track of hops
hops = []

for elem in list_to_search:
  # f is element of found and h is element of hops
  print(elem)
  f,h = sl.search(elem)
  found.append(f)
  hops.append(h)

print(hops)
print(f"Wrong searches = {found.count(0)}")
print(f"Average Hops = {sum(hops)/n}")