print("Welcome to Python Pizza Deliveries!")
size =  input("What size pizza do you want? S, M or L: ")
peperonni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")

bill = 0 
if size == "S": 
    bill += 15
elif size == "M": 
    bill += 20
elif size == "L":
    bill += 25
else: 
    print("You typed the wrong inputs.") 

# If the user wants peperoni on the pizza 
if peperonni == "Y": 
    if size == "S": 
        bill += 2 
    else: 
        bill +=3 

# if the user wants extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill} ")

