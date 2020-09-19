def factorial(number):
    if number < 0:
        print('Invalid entry! Cannot find factorial of a negative number')
        return -1
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def factorial_iteration(number):
    if number < 0:
        print('Invalid entry! Cannot find factorial of a negative number')
        return -1
    fact = 1
    while(number > 0):
        fact = fact * number
        number = number - 1
    return fact

if _name_ == '_main_':
    userInput = 8
    print('Factorial using Recursion of', userInput, 'is:', factorial(userInput))
    print('Factorial using Iteration of', userInput, 'is:', factorial_iteration(userInput))
