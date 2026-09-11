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

# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
# def main() -> None:
 #   """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input(How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
# if __name__ == "__main__":
#    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
