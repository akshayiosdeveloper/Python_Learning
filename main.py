import random

# variable declaration 
player_choice = "rock"
print(player_choice)

# functions declaration
def get_choices():
    player_choice = 'akshay'
    return player_choice  

def greeting():
    return 'Hi'

# function calling 
response  = greeting() 
print(response)

response1 = get_choices()
print(response1)

# dictionaries 
dict = {"name": "Akshay🎾hod ", "color": response}
# How to get dictionaries values
player_name = dict["name"]
print(player_name)

def function_return_dictionary():
    #input_choice = input("Enter a choice (rock, paper ,comb)")
    company = "S"
    id = 115
    choices = { "company" : company , "id": id}
    return choices

result = function_return_dictionary()
print(result)
    
#   List or Array
food = ["pizza","carrots","eggs"]  
dinner = random.choice(food)
print(dinner)

# function with parameters
def check_win(player, computer):
    print(f"You choose {player}, computer choose {computer}")
    return[player, computer]
check_win(["a,b"],{"a": 1 , "b": 2})

age = 13 
if age >= 18:
    print("You are baby")
    if age < 15:
        print("You are teenager!!!")
elif age > 12:
    print("You are teenager")
else:
    print("you are toddler")        
#strings 
# When we do modification in a string it always return a modified string
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