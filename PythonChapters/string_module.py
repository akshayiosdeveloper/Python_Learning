#strings 
# When we do modification in a string it always return a new string object /instance not the old one
"Akshay"
'Aksahy'
phrase = "akshay" + "Kumar"
print(phrase)
agee = 34
age1 = str(agee)
print(age1)
print(""" 39  years old """)
print("akshay".upper())
print("kumar".capitalize())
name1 = "AK"
print(name1.lower())
print(name1)
print(len(name1))
print("au" in name1)
# SPECIAL CHARACTER BACKSLASH \ FOR PRINTING QUOTES ETC
str1 = 'AKS\"HAY'
print(str1)
# GET THE INDEX OF STRING
index = str1[2]
print(index)
print(str1[2:5])
print(str1[1:]) # it will print starting till end becuase : will print entire stirng

# boolean 
done = 5
if done:
    print("yes") 
else:
    print("no")    