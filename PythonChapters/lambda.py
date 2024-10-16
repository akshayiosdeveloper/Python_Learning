
#A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


x = lambda a : a + 10
print(x(10))

x = lambda a, b : a * b
print(x(6,6))

# Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
    return lambda a : a * n

lambdaobj = myfunc(2)
mytripler = myfunc(3)

print(lambdaobj(11))
print(mytripler(10))