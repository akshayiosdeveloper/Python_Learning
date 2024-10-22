 # variable is only available from inside the region it is created. This is called scope.
def myfunc():
  x = 300
  print(x)

myfunc() 

def myfunc1():
  x = 500
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc1()

xx = 300

def myfunc2():
  xx = 2000
  print(xx)

myfunc2()

print(xx)

# The global keyword makes the variable global.

def myfunc23():
  global obj
  obj = 4500

myfunc23()

print(obj)