# sanity: check for any other inputs than those given and make sure not crashed
# TODO OPTION B AND D(optional)
    # make func to get header and other info from DefaultRecords
    # make func to check validity


from add_a_new_expense import add_new_expense                   # option a
from search_mod_expense import search_mod_expense               # option b
from add_category_name_method import add_categ_name_method      # option c

# import datetime
# import calendar
# import string
# import csv
import os
import re


# ------------------------------------------------- Main Menu Program -------------------------------------------------_
prog_stop = False
while not(prog_stop):

    # main menu of options
    print("\nMain Menu _______________________________________________________________________________________________")
    print(" a. Add a new expense")
    print(" b. Search/Modify an expense")
    print(" c. Add an expense category or expense name")
    print(" d. Import expense data (optional for bonus points)")
    print(" e. Close the program")

    # user input of option
    option = input("Type in a letter a-e to chose an option: ")

    if option == "a":
        add_new_expense()
    elif option == "b":
        search_mod_expense()
    elif option == "c":
        add_categ_name_method()
    elif option == "d":
        print("")
        # run func
    elif option == "e":
        prog_stop = True
        break
    else:
        print("That is not a valid option, try again.\n")

