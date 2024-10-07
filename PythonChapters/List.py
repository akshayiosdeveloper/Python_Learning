items = ["a" ,"d" ,"b","f" ,"c","A" ,"B"]
print("---length func---")
print(len(items))
print("---sort---")
#items.sort()
items.sort(key=str.lower)

print(items)

# Access items 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# add items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
# loop through list 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print("index: "+ str(i)+  " " +thislist[i])
  #List Comprehension
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)    

