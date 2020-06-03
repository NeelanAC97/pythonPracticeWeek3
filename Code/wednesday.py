
n = int(input("Enter a number: "))

dictionary = {}

def add_to_dictionary(n):

    for i in range(1,n+1):
        dictionary[i] = i*i

    return(dictionary)

print(add_to_dictionary(n))

"""try:
    
    n = int(input("Enter a number: "))

    dictionary = {}

    def add_to_dictionary(n):

        for i in range(1,n+1):
            dictionary[i] = i*i

        return(dictionary)

    print(add_to_dictionary(n))

except ValueError:
    print("that is not a valid number")
except NameError:
    print("that is not a valid number")
except TypeError:
    print("that is not a valid number") """


    
