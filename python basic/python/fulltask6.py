# 1. Review system, the stars typically represent the different levels of satisfaction.
# Start by creating a rating variable and set it equal to a decimal number.
# Make a rating system using an if/elif/else statement:
# rating greater than 4.5, print 'Extraordinary'
# rating greater than 4, print 'Excellent'
# rating greater than 3, print 'Good'
# rating greater than 2, print 'Fair'
# Everything else, print 'Poor'


rate=float(input("Enter the score:"))
try:
    def rev(rate):
        if rate>=4.5 and rate<=5:
            print("extraordinary")
        elif rate>=4 and rate<=4.5:
            print("excellent")
        elif rate>=3 and rate<=4:
            print("good")
        elif rate>=2 and rate<=3:
            print("fair")
        else:
            print("poor")
except ValueError:
    print("Value error")
rev(rate)


# 2. Use the random module to create a number from 0 to 5.
# Then use an if/elif/else statement to print out one of these six random facts:
# 0 - 'Flamingos turn pink from eating shrimp.'
# 1 - 'The only food that doesn\'t spoil is honey.'
# 2 - 'Shrimp can only swim backwards.'
# 3 - 'A taste bud\'s life span is about 10 days.'
# 4 - 'It is impossible to sneeze while sleeping.'
# 5 - 'It is illegal to sing off-key in North Carolina.'



num=[1,2,3,4,5]
choice=int(input("enter choice from 0-5:"))
def numb():
    if choice == 0:
        print('Flamingos turn pink from eating shrimp.')
    elif choice == 1:
        print('The only food that doesn\'t spoil is honey.')
    elif choice == 2:
        print('Shrimp can only swim backwards.')
    elif choice == 3:
        print('A taste bud\'s life span is about 10 days.')
    elif choice == 4:
        print('It is impossible to sneeze while sleeping.')
    elif choice == 5:
        print('It is illegal to sing off-key in North Carolina.')
    else:
        print("Wrong Choice")
numb()


# 3. Instructions
# four seasons in the year — winter, spring, summer, or fall
# Ask the user the month number using the input() function.
# Check for the four seasons using an if/elif/else statement and logical operators:
# month is 1, 2, 3, print 'Winter'
# month is 4, 5, 6, print 'Spring'
# month is 7, 8, 9, print 'Summer'
# month is 10, 11, 12, print 'Autumn'
# Everything else is 'Invalid'



month = int(input("Enter the month number (1-12): "))
def mon(month):
    if month == 1 or month == 2 or month == 3:
            print('Winter')
    elif month == 4 or month == 5 or month == 6:
            print('Spring')
    elif month == 7 or month == 8 or month == 9:
            print('Summer')
    elif month == 10 or month == 11 or month == 12:
            print('Autumn')
    else:
            print('Invalid')
mon(month)


# 4. Create a weight conversion program that:
# Asks the user what their Earth weight is (as a float).
# Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.
# To calculate the user's weight:
# destination weight=Earth weight × relative gravity
# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14
# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

user_weigh=float(input("Enter weight:"))
planet_num=int(input("Enter a planet num from 1-7:"))
def weight():
    if planet_num == 1:
        dest_weight = user_weigh * 0.38
        print('Mercury weight:', dest_weight)
    elif planet_num == 2:
        dest_weight = user_weigh * 0.91
        print('Venus weight:', dest_weight)
    elif planet_num == 3:
        dest_weight = user_weigh * 0.38
        print('Mars weight:', dest_weight)
    elif planet_num == 4:
        dest_weight = user_weigh * 2.53
        print('Jupiter weight:', dest_weight)
    elif planet_num == 5:
        dest_weight = user_weigh * 1.07
        print('Saturn weight:', dest_weight)
    elif planet_num == 6:
        dest_weight = user_weigh * 0.89
        print('Uranus weight:', dest_weight)
    elif planet_num == 7:
        dest_weight = user_weigh * 1.14
        print('Neptune weight:', dest_weight)
    else:
        print('Invalid planet number')
weight()


# 6. a countdown from 10 to 1.
# Use a for loop that counts down by using the "step" value in range().
# Inside the loop, print the numbers from 10 to 1, each on its own line.
# When the loop finishes the countdown, print this exact string.


for i in range(10, 0, -1):
    print(i)


print("Blastoff!")


# 7. Suppose we have a pair of dice.
# First, use the random module to “roll” the two dice.
# Each die (named die1 and die2) should have an integer value from 1 to 6.
# Store the sum of the two random values in variable named total.
# Using a while loop, check if total is 2. If it isn't, print the string 'Nope' and keep "rerolling" the dice.
# Let the loop run until the total is 2, then print 'Snake eyes!

import random

def play_game():
    while True:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        
        if total == 2:
            print('Snake eyes!')
            break  
        else:
            print('Nope')

play_game()


# 8. Find the sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)

# 9. Sum of even numbers from 1 to 50
esum = 0
for i in range(2, 51, 2):
    esum += i
print(esum)


# 10. Sum of odd numbers from 1 to 50
odd_sum = 0
for i in range(1, 51, 2):
    odd_sum += i
print(odd_sum)



# 11. Sum of all numbers in a list
numbers = [10, 20, 30, 40, 50]
total_sum = 0

for num in numbers:
    total_sum += num
print(total_sum)


# 12. Define a word and print each character
word = "Python"

for char in word:
    print(char)


# 13. Find the largest number in a list
numbers = [14, 52, 5, 89, 32, 11]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print(largest)


# 14. Count how many even numbers exist in a list
numbers = [3, 8, 12, 5, 7, 20, 11]
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(even_count)
