#def is_prime(x):
#    if x < 2:
#        return False
#    else:
#        for n in range(2, x-1):
#            if x % n = 0:
#                return False
#            return True

import pdb

pdb.set_trace()

def is_prime(x):

    if x < 2:
        return False
    elif x == 2:        # previously returning "None" for x = 2
        return True     #####
    elif x == 3:        # previously returning "None" for x = 3
        return True     #####
    else:
        for n in range(2, x-1):
            if x % n == 0:      #####
                return False
            return True

a = is_prime(7)
b = is_prime(8)
c = is_prime(1)
d = is_prime(3)
e = is_prime(2)