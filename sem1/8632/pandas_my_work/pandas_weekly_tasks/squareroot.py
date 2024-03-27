import math

def sqrt(num):
    """
    Function which takes num argument and returns approximate square root using Newton's method.
    """

    #Deal with negative case.
    if num < 0:
        return "Number is negative. Enter a positive number."
    
    guess = num / 2

    #Implement Newton's method
    while True:
        new_guess = 0.5 * (guess + num / guess)

        #Define precision
        if abs(new_guess - guess) < 0.0001:
            return new_guess
        
        guess = new_guess

def main():
    value = float(input("Please enter a positive number:"))

    approximate_sqrt = sqrt(value)

    print("The square root of %s is approx %s" % (value, approximate_sqrt))

if __name__ == '__main__':
    main()