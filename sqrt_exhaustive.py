#Author: Nicholas Moreno 
# We need an integer, converting string input
def sqrt_exhaustive(x):
    """ Search for perfect squre of x 
        x(int) : positive number
        return guess(int): positive number
        """

    #guess=0

    # Searching starting at 0 for proper square root of x
    for guess in range(x):
        if guess**2 == x:
            return guess
    
    
    return None
    #while guess**2 < x:
     #   guess = guess + 1
    
    #if guess**2 == x:
     #   return guess
    #else:
     #   return None

user_number = int(input("Enter a positive integer: "))

guess = sqrt_exhaustive(user_number)

# Need to check if search was successful
if guess**2 != None:
    print("Square root of {} is {}".format(user_number, guess))
else:
    print("No square root found for {}".format(user_number))