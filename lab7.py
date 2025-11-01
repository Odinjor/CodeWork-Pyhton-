# STUDENT name: Ugochukwu Odinjor
# Email: uodinjor1@student.gsu.edu
# CSCI 1301 – 52074
# Python Lab 7
# References: no one

'''
o Purpose: offer the user a choice of food items, calculate total bill
o
Pre-conditions: user enters 5 or 6 y's or n's depending on desired items
(strings)
o
Post-conditions: prompts for choices, total bill before (float) and after
tip, (float)
o and parting message.
o '''
print('Welcome to Dairy King')

food_items = {'Grilled Cheese': 7, 'Nachos': 5, 'Chicken': 8, 'Hamburger': 8, 
              'Cheeseburger': 10, 'Hot Dog': 6}
print('Please answer each questions with y or n')
order = ''
total = float(0)
while order != 'n':
    order = input('Do you want a grilled cheese?')
    if order == 'y':
        total += food_items['Grilled Cheese']
    order = input('Do you want a serving of nachos?')
    if order == 'y':
        total += food_items['Nachos']
    order = input('Do you want a chicken sandwich?')
    if order == 'y':
        total += food_items['Chicken']
    order = input('Do you want a hamburger?')
    while order == 'y':
        order = input('Do you want cheese on that?')
        if order == 'y':
            total += food_items['Cheeseburger']
            break
        else:
            total += food_items['Hamburger']
    order = input('Do you want a hotdog?')
    if order == 'y':
        total += food_items['Hot Dog']
    break

print(f'The total for your food is ${total:.2f}')
print(f'The total with 20% tip is ${total + total * .2:.2f}')
print('Thank you for your business!')


