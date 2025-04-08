# Basic function
def basic_function():
    print("This is a basic function.")

# Function with parameters
def function_with_parameters(param1, param2):
    print(f"This is a Function with parameters. Parameter 1: {param1}, Parameter 2: {param2}")

# Function with default parameters
def function_with_default_parameters(param1, param2=10):
    print(f"This is a Function with default parameters. Parameter 1: {param1}, Parameter 2: {param2}")

# Function with variable number of parameters tuple
def function_with_variable_parameters(*args):
    print("Function with variable number of parameters tuple:", args)

# Function with varirable number of parameters dictionary
def function_with_variable_parameters_dict(**kwargs):
    print("Function with variable number of parameters dictionary:", kwargs)

def function_with_return_value(major, **student):
    student['major']=major
    return student, major


#Function calls  
#basic_function() 
# function_with_parameters('param1', 'param2')
# function_with_parameters(param2='2', param1=1)
# function_with_default_parameters('param1')
# function_with_default_parameters('param1', 'param2')
# function_with_variable_parameters(1,2,3,True)
# function_with_variable_parameters_dict(name='Alice', age= '25')
output, major=function_with_return_value("Computer Science",name='Alice', age= '25')
print(f"This is a Function with return value. Output: {output}, Major:{major}")

# construct  used to ensure that a certain block of code is executed only when the script is run directly
# if __name__ == "__main__":
#    basic_function() 
