# CHALLENGE OF THE DAY

# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a 
# comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output 
# should be: 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def factorial_func(num):
    
    if num < 0:
        return print("Sorry, factorial does not exist for negative numbers")
    
    elif num == 0:
        return print("The factorial of 0 is 1")
    
    else:
        factorial = 1
        
        for i in range(1,num + 1):
            factorial = factorial*i

        return factorial

factorial_list = []

for i in range(3):
    
    number = int(input("Enter a number: "))
    factorial_list.append(factorial_func(number))

print(factorial_list)
   
