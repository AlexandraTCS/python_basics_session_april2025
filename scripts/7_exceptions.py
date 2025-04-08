
def divide_basic(y):
    try:
        result = 10 / y
        print(f'Result is: {result}')
    except :
        print("Something went wrong!")


def divide_advanced(y):
    try:
        result = 10 / y
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except TypeError:
        print("You can only divide by numbers!")
    else:
        print("Result is:", result)
    finally:
        print("This code runs no matter what!")

def divide_all_errors(y):
    try:
        result = 10 / y
    except Exception as e:
        print(f"An error occurred: {e}")



#divide_basic(2)
#divide_basic(0)
#divide_advanced('u')
#divide_advanced(0)
#divide_advanced(2)
divide_all_errors("u")