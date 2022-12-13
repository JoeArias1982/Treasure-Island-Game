print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Player_1 = input(
    "You have arrived at the beach, you have to make a choice to go Left or Right on the first. (L or R)?\n"
).upper()
#Player_2 = input("You have arrive at the beach, you to make a choice to go Left or Right on the first. (L or R)?\n")

if Player_1 == "R":
    print("\nYou have come across a canal, will you SWIM or WAIT?\n")
    Player_1 = input(("S or W?\n")).upper()
    if Player_1 == "S":
        print(
            "\n!!!GAME OVER!!!\nYou were EATEN by a SHARK!!!\n<Tuhhhnaa Tuhhhnaa Tuhhhnaa>\n"
        )
    elif Player_1 == "W":
        print(
            "\nYou have waited and decided not to swim, now in the moonlight you see a three different color doors appear.\nPick RED Door or BLUE Door or YELLOW Door?\n"
        )
        Player_1 = input("R or B or Y?\n").upper()
        if Player_1 == "Y":
            print("\nYou have found the MATRIX Door!\n YOU WIN!!!\n")
        elif Player_1 == "R":
            print(
                "\nGAME OVER!!!!\nYou have fallen into a FIRE PIT!!!\n<TOASTY>\n"
            )
        elif Player_1 == "B":
            print(
                "\nGAME OVER!!!! You were EATEN by a pack of Wolf's!!!\n<Ruff Ruff Ruff>\n"
            )
else:
    print("\nGAME OVER!!!! YOU FELL INTO A HOLE\n")

#Class Version Below

choice1 = input(
    'You\'re at a crossroad, where do you want to go? Type "left" or "right".\n'
).lower()

if choice1 == "right":
    choice2 = input(
        'You\'ve come to a Lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim             accross.\n'
    ).lower()
    if choice2 == "wait":
        choice3 = input(
            "You have arrived at the island unharmed. There are 3 doors. One is Red, Oneis Yellow, One is Blue. Which color door will you        choose?\n"
        ).lower()
        if choice3 == 'red':
            print("It's a room full of FIRE. Game Over.")
        elif choice3 == 'yellow':
            print("You found the Treasure! YOU WIN")
        elif choice3 == 'blue':
            print("You entered a room full of BEASTS. GAME OVER")
    else:
        print("You have attacked by an ANGRY THROUT. GAME OVER")
else:
    print("You fell into a HOLE. Game Over.")
