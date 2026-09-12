#Calculate users birth year with name and age which they input.

#Input:
  #  String: Name entered by user
    # Interger: Age ented by user
   # Third input not required we only need name and age

#Process:
 #   Subtract age from the current year given by the imported date and time

#Output:
 #   Printed name and age of the person

#Typical usage example:
#    What is your name? Sutton
 #   How old are you? 25
  #  Hello Sutton! You were born in 2001. 

from datetime import datetime‹

CURRENT_YEAR = date.now().year  

    name = input("What is your name? ")
    age = int(input(How old are you? "))

    birth_year = CURRENT_YEAR - age

    print(f"Hello {name}! You were born in {birth_year}.")




