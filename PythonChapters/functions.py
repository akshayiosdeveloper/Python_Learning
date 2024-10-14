# In Python a function is defined using the def keyword:
def my_function():
    print("hello function !!!!!")
    
my_function()    
# Arguments
def func_with_arguments(fname):
    print("You typed:" + fname)    
    
func_with_arguments("akshay")
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly: 

# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)
  
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")     
# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

#To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
  print(x)

my_function(3)