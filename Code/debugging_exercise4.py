#item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
#n = 0

#while n < 5:
#    for i in item_list:
#        print(item_list[i])

#print item_list[5]

import pdb

pdb.set_trace()

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
   for i in item_list:
        print(i)    # previously getting error: "TypeError: list indices must be integers or slices, not str"
    n += 1          # previously was an infinite loop

print(item_list[4]) # previously index out of range

