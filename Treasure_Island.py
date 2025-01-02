print('''
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcone to Treasure Island")
print("Your mission is to find the treasure.")
choice1 = input('Youre at a crossroad, where do you want to go? "Left" or "Right". ').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake, there is an island in the middle ' 
          'of the lake. Type "Wait" to wait. Type "swim" to swim ' 
          'across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with three doors," 
              "one red, one yellow, and one blue. Which door do you choose? ").lower()
        if choice3 == "Red": 
            print("You fell into a pit of fire. Game over")
        elif choice3 == "Yellow": 
            print("You have found the treasure! Congratulations")
        elif choice3 == "Blue": 
            print("You fell into into a deep pool")
        else: 
            print("You chose a door that does not exist.")
    else: 
        print("You got attacked by an angry troll. Game over")
else: 
    print("Game Over")