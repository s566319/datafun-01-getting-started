"""
Purpose: This script will ask users how much are they willing to spend for their tickets to travel to Latvia.

Author: Inga Miller
44-608, Fundamentals of Data Analytics 
Project 1

"""
# Record your work automatically with our datafun logger
from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)

print('How much would you pay for a ticket to travel to Latvia?!')

# Get ticket cost information from the user

number1 = int(input('700: '))
number2 = int(input('1300: '))
number3 = int(input('1800: '))

# read first integer
number1 = int(input('How much would you pay for a ticket: '))

# read second integer
number2 = int(input('How much would you pay for a ticket: '))

#read third integer
number3 = int(input('How much would you pay for a ticket '))

#Calculate several statistics

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)

"""Find the minimum one would pay for the tickets."""

number1 = int(input('700: '))
number2 = int(input('1300: '))
number3 = int(input('1800: '))

minimum = number1  

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

number1 = int(input('700: '))
number2 = int(input('1300: '))
number3 = int(input('1800: '))

string1 = input ("Please enter minimum you would pay:")
string2 = input ("Please enter the maximum you would pay:")
string3 = input ("Please enter how much money you have in your bank account currently:")

int1 = int(string1)
int2 = int(string2)
int3 = int(string3)

logger.info(f" your interesting results here") 

"""Find the maximum one would pay for the ticket prices."""

number1 = int(input('1800: '))
number2 = int(input('1300: '))
number3 = int(input('700: '))

minimum = number1  

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3
    
number1 = int(input('700: '))
number2 = int(input('1300: '))
number3 = int(input('1800: '))
total = 700 + 1300
total


"""Find the maximum one would pay for the ticket prices."""

number1 = int(input('1800: '))
number2 = int(input('1300: '))
number3 = int(input('700: '))

minimum = number1  

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3
    
number1 = int(input('700: '))
number2 = int(input('1300: '))
number3 = int(input('1800: '))
total = 700 + 1300
total

#log the results

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())


