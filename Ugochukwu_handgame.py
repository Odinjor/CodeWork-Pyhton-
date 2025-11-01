import random
print('The Rock Paper Scissors Game')
print()
rock = 1
paper = 2
scissors = 3
user_input = 0
while user_input != -1:
    user_input = int(input('Enter 1 for rock, 2 for paper, 3 for scissors or -1 to quit the game. '))
    print()
    computer_choice = random.randint(1,3)
    if user_input != -1:
        if user_input == rock:
            print('You chose rock')
            print()
        elif user_input == paper:
            print('You chose paper')
            print()
        elif user_input == scissors:
            print('You chose scissors')
            print()
        if computer_choice == rock:
            print('The computer chose rock')
            print()
        elif computer_choice == paper:
            print('The computer chose paper')
            print()
        elif computer_choice == scissors:
            print('The computer chose scissors')
            print()
        if (user_input == rock and computer_choice == paper) or (user_input == paper and computer_choice == scissors) or (user_input == scissors and computer_choice == rock):
            print('Sorry you lose!')
            break
        elif (user_input == rock and computer_choice == scissors) or (user_input == paper and computer_choice == rock) or (user_input == scissors and computer_choice == paper):
            print('Congratulations you win!')
            break
        if user_input == computer_choice:
            print('The match was a tie!')
            break
    else:
        print('Goodbye')
