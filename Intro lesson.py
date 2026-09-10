# BTEC Programming - Lesson 1: Introduction to Python

# This is a comment. Python ignores it. Use comments to explain your code!
# comment out all of the below text by selecting everything and pressing Ctrl + / (or Cmd + / on Mac)
# MAKE LOTS OF COMMENTS TO EXPLAIN YOUR CODE!

# These lines should be a comment. or "hashed out"
# As long as this is not a comment it will interupt the Code as the computer attempts to read it.
# It will produce an error. 
# Each line starting with "#" is regarded a comment. # even if it follows after a line. After hashing out
# you can try the script by pressing the run code button(the triangle button) in the top right corner of the screen.


# 1. Printing text to the screen:  A string is a sequence of characters: often words or sentences. By using the print function, we can display text on the screen.
# you can display the text on the terminal. A string is between "" or '', please write hello world and press run code.
print("")

# 2. Variables and assignment. A variable can be used to store a string or number (or other data types). 
# You can think of a variable as a box that holds a value. You can name the variable anything you like, but it must start with a letter or underscore and cannot contain spaces
# Best practice is to use "camelcase" for variable names, which means starting each new word with a capital letter, like this: myVariableName or myName.

name = "Student"    # Assigns the string 'Student' to the variable name
age = 16            # Assigns the number 16 to the variable age

print("My name is", name)
print("I am", age, "years old.")

# 3. User input: The variable will be whatever the user types in response to the prompt.
your_Name = input("What's your name? ")
print("Nice to meet you,", your_Name + "!")

# 4. Simple math is doen by numbers instead of strings. Int stands for integer, which is a whole number.
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
sum = number1 + number2
print("The sum of your numbers is:", sum)

# 5. Mini Challenge
# Can you change the code below to multiply the two numbers instead of adding them?
product = number1 + number2
print("The product of your numbers is:", product)