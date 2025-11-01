# Prolog
# Author: Ugochukwu Odinjor
# Email: uodinjor1@student.gsu.edu
# Section: 002
'''
Purpose:
calculate the change you are due when you buy an item in a store
Pre-conditions (input):
money given to the cashier(cost of item)
Post-conditions (output):
 change user get back from the cashier(dollars, quarters, dimes, nickels and
pennies)
'''
def main():
# Design and implementation
# 1. Output a message to identify the program, and a blank line
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
    print()
# 2. Input amount of change from user
    amt = int(input('Enter the change amount:'))
    cost = float(input('Enter cost of an item: '))
# 3. Calculate the change
    import math
    change = amt - cost
    dollars = int(change // 1.00)
    quaters = int(change % 1.00 // .25)
    dimes = int(change % 1.00 % .25 // .10)
    nickel = int(change % 1.00 % .25 % .10 // .05)
    pennies = int(round(change % 1.00 % .25 % .10 % .05 / .01))
    


# 4. Output resulting change and given cost of an item
    print()
    print( f"change is converted to dollars= {dollars}, quaters= {quaters}, dimes= {dimes}, nickels= {nickel}, pennies= {pennies}")
main()
''' The first syntax error we have is in line 17-18. A part of the print function is misplaced.
    In addition, the two print functions were not indented correctly.
    For the amt variable the string inside the input function did not have the right quotation.
    After figuring out the formula for the change conversion the only problme I had was getting the penny conversiob right, so I just chose to divide it normally and round up. 
    Also changine the print format. If you could give me an explanaton on how % and // I would deeply appreciate it even though I got it to work I'm still having a hard time understanding it. '''
# end of program file
