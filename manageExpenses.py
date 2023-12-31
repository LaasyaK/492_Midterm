"""
Author: Laasya Kallepalli
Date: 6/20/2023
Purpose: Main program that runs the main menu to run each option
Input(s): can take 1 commandline argument ('--report' or '--graph') to run other menus
Output(s): takes user to the other functions
"""

import sys
import re
import platform
from MainMenuOptions import add_new_expense                     # option a
from MainMenuOptions import search_mod_expense                  # option b
from MainMenuOptions import add_categ_name_method               # option c
from ReportAndGraphFunctions import report                      # report function
from ReportAndGraphFunctions import graph                       # graph function




# ------------------------------------------------- Main Menu Program --------------------------------------------------

# telling user to download 3rd party library
print("*** Before the Program can run, make sure you have installed matplotlib. Some functions will not run "
      "without this library. ***")

# taking the arguments to run different functions if typed in
if len(sys.argv) > 1:
    option = sys.argv[1]
    try:
        option_temp = re.search(r"\-\-(.*)", option)
        option = str(option_temp.group(1))
        if option == "report":
            report()
        elif option == "graph":
            graph()
        else:
            print("The argument passed is not valid, available arguments are '--report' and '--graph'.")
            exit(0)
    except ValueError:
        print("The argument passed is not valid, available arguments are '--report' and '--graph'.")
        exit(0)

# running the main menu
prog_stop = False
while not(prog_stop):

    # main menu of options
    print("\nMain Menu _______________________________________________________________________________________________")
    print(" a. Add a new expense")
    print(" b. Search/Modify an expense")
    print(" c. Add an expense category or expense name")
    print(" e. Close the program")

    # user input of option
    option = input("Type in a letter a-e to chose an option: ")

    if option == "a":
        add_new_expense()
    elif option == "b":
        search_mod_expense()
    elif option == "c":
        add_categ_name_method()
    elif option == "e":
        prog_stop = True
        break
    else:
        print("That is not a valid option, try again.\n")
