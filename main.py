from knapsack import *
from ks_utils import *
from my_tests import *

#Check my tests
tests = TestKSP()
tests.test_from_data_to_item()
tests.test_4() 
# ..                        # Add more tests as you consider convenient

first_line = input().split() # N items, Capacity
item_count = int(first_line[0])
capacity = int(first_line[1])

items = []
for i in range(1, item_count+1):
    parts = input().split() # CSV
    items.append(Item(i-1, int(parts[0]), int(parts[1])))

value, taken = solve_exam(items, capacity)

print(check_solution(capacity, items, taken), end='')
print(taken_items(items,taken))
