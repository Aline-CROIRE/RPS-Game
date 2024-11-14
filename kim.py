import random
user_choice = int(input("enter your choice 0 for rock,1 for paper,2 for scissors"))
computer_choice = random.randint(0,2)
if user_choice >= 3:
    print("you entered invalid choise!, you lose!")
else:
    print(f"you choose{user_choice}")
    print(f"computer choose{computer_choice}")

    if computer_choice == user_choice:
        print('its a draw')
    if computer_choice == 0 and user_choice == 2:
        print('you win!')
    elif computer_choice == 2 and user_choice == 1:
        print('you lose!')
    elif computer_choice > user_choice:
        print('you win!')



