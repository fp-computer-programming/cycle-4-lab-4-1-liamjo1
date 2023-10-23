"""
Create a Python file named lab_4-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Prompt the user to enter their first name and store it with an appropriate variable.
Prompt the user to enter their last name and store it with an appropriate variable.
Create a new variable for the user's full name and set it equal to the first name variable plus the last name variable. What is the result?
Is there an issue with this output? How could we fix that?

"""
# Liam O'Hara

first_name = input("Please enter your first name:")
# Prompt user for first name - Liam O'Hara

last_name = input ("Please enter your last name:") 
# Prompt user for last name - O'Hara

full_name = first_name + last_name  
# Combine both variables into one full name - Liam O'Hara 
print(full_name)

# The output does not have a space between the first and last name.
# We could fix that by including a space between the first_name and last_name variables.