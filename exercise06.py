def game(my_chances,Total_chances,my_points,comp_points):
    print("----- Welcome to Snake, Water and Gun game🐍💦🔫 -----\n")
    print('''for Snake: s,
for Water: w,
for Gun: g.\n''')
    import random
    lst = ['s','w','g']

    while my_chances<Total_chances:
        comp_input = random.choice(lst)
        userInput = input("Enter the correct key-- Snake(s), Water(w), Gun(g):\n").lower()
        if userInput in lst:
            if userInput == comp_input:
                print(f"The game is Tie...\nComputer's points is {comp_points} and,\nUser point is {my_points}.\n")
            elif userInput == 's' and comp_input == 'w':
                my_points += 1
                print(f"Congrats User Won...\nBecause computer's input is {comp_input}\nUser's point is {my_points}\nComputer's point is {comp_points}\n")
            elif userInput == 'w' and comp_input == 'g':
                my_points += 1
                print(f"Congrats User Won...\nBecause computer's input is {comp_input}\nUser's point is {my_points}\nComputer's point is {comp_points}\n")
            elif userInput == 'g' and comp_input == 's':
                my_points += 1
                print(f"Congrats User Won...\nBecause computer's input is {comp_input}\nUser's point is {my_points}\nComputer's point is {comp_points}\n")
            else:
                comp_points += 1
                print(f"Sorry!, You loose..\nBecause computer's input is {comp_input}\nUser's points is {my_points} and,\nComputer's point is {comp_points}\n")
        else:
            print("Sorry!.. Invalid input.")
        my_chances += 1
    
    if my_points == comp_points:
        print("The game is Tie..")
    elif my_points>comp_points:
        print(f"Congrats.. You won by {my_points},{comp_points}")
    else:
        print(f"Sorry!..You Loose by {my_points},{comp_points}")

my_chance = 0
Total_chance = 5
my_point = 0
computer_point = 0
game(my_chance,Total_chance,my_point,computer_point)
