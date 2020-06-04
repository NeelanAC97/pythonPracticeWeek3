# Python CHALLENGE OF THE DAY
 
# Question: Write a program which will find all such numbers 
# which are divisible by 7 but are not a multiple of 5, between 
# 2000 and 3200 (both included). The numbers obtained should be 
# returned in a comma-separated sequence on a single line.

# Hints: Consider use range(#begin, #end) method

numbers = []

for i in range(2000, 3201):
    
    if i % 7 == 0 and i % 5 != 0:  
        numbers.append(i)
    else: 
        continue

print(numbers)