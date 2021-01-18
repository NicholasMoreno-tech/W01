#Author: Nicholas Moreno
# We need an Real Number, converting string input
def sqrt_exhaustive(x:float, epsilon:float=0.01):
    """ Search for perfect squre of x 

        x(int) : positive number
        epsilon (float): precision

        return guess(int): square root or none
    """

    guess=0

    step = epsilon*epsilon
    
    while abs(guess**2 - x) > epsilon:
        guess = guess + step
    
    if abs(guess**2 - x) <= epsilon:
        return guess
    else:
        return None

user_number = float(input("Enter a positive real number, e.g 3.0: "))

guess = sqrt_exhaustive(user_number)

# Need to check if search was successful
if guess**2 != None:
    print("Square root of {} is {}".format(user_number, guess))
else:
    print("No square root found for {}".format(user_number))