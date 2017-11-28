"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
"""

# Check if the given number is a prime
# And return a message that says it is or isn't
def check_prime(number):

    for i in range(2, number - 1):
        if number % i == 0:
            return "The number {} is not a prime!".format(number)
    return "The number {} is a prime!".format(number)

# Ask the user for his input
# If user input is quit leave the program
# If user input is not quit 
# start the function that checks if the number is a prime
while True:
    number = input("Give me a number or type 'Quit' to quit \n > ").lower()
    if number == "quit":
        break
    else:
        number = int(number)
    print(check_prime(number) + "\n")
