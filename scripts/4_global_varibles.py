x='Global variable'

def function_with_local_variable():
    x = 'Local variable'  # This x is local to the function
    print(f"Inside function: {x}")

print(f"Outside function: {x}")  # This will print the global variable

def function_with_global_variable():
    global x  # Declare x as global to modify the global variable
    x = 'Modified global variable'
    print(f"Inside function: {x}")
    
print(f"Outside function: {x}")  # This will print the global variable

#function_with_local_variable()    
function_with_global_variable()
print(f"Outside function: {x}")  # This will print the modified global variable