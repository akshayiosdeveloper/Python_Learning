f = open("/Users/akshaykumar/python/Python_Learning/PythonChapters/demofile.txt","r")
# for x in f:
#   print(x)
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("/Users/akshaykumar/python/Python_Learning/PythonChapters/demofile.txt", "r")
print(f.read())
