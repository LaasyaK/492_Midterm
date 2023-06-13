# sanity: check for any other inputs than those given and make sure not crashed
# TODO OPTION B AND D

from add_a_new_expense import add_new_expense                   # option a
from add_category_name_method import add_categ_name_method      # option c

# import datetime
# import calendar
# import string
# import csv
import os
import re



# getting the header, expense_category, names, and payment_method info from DefaultsRecord
with open("DefaultsRecord.txt", 'r', newline='') as defaults:

    # read all contents of txt
    content = defaults.read()
    groups = re.findall(r'\[(.*?)\]', content)

    # put each group found to list name
    header = []
    header = re.findall(r'\"(.*?)\"', groups[0])

    Expense_category = []
    Expense_category = re.findall(r'\"(.*?)\"', groups[1])

    Expense_name = []
    Expense_name = re.findall(r'\"(.*?)\"', groups[2])

    Payment_Method = []
    Payment_Method = re.findall(r'\"(.*?)\"', groups[3])


# -------------------------------------------- Main Menu Options Functions ---------------------------------------------

# searches and modifies an expense in a datasheet
def search_mod_expense():
    print("\nSearch/Modify an expense Function _______________________________________________________________________")

    # ask user for search criteria in a format
    print("Type in what search criteria you want to search for by typing Field:Data, Field:Data, Field:Data, etc.")
    print("For example: Year:2020, Month:May, Expense_Category:Utility, Payment_Method:Check (make sure if field has 2 "
          "words put an '_' between the words, capitalize field and data entries, and add a ',' to every new field "
          "entry, or type 'main' to return to the main menu.)")
    search_crit = input("Type here: ")

    # getting search object from user input
    year_input = re.search(r"Year:(.*?)(?=,)", search_crit)
    month_input = re.search(r"Month:(.*?)(?=,)", search_crit)
    categ_input = re.search(r"Expense_Category:(.*?)(?=,)", search_crit)
    name_input = re.search(r"Expense_Name:(.*?)(?=,)", search_crit)
    due_input = re.search(r"Amount_Due:(.*?)(?=,)", search_crit)
    date_input = re.search(r"Due_Date:(.*?)(?=,)", search_crit)
    paid_input = re.search(r"Amount_Paid:(.*?)(?=,)", search_crit)
    pay_due_input = re.search(r"Payment_Date:(.*?)(?=,)", search_crit)
    method_input = re.search(r"Payment_Method:(.*?)(?=,)", search_crit)

    # if user types main, function stops
    if search_crit == "main":
        return 0

    # if year data exists, find if a file for that year exists
    if not(year_input == "None"):
        year_search = year_input.group(1)
        current_folder = os.path.dirname(os.path.abspath(__file__))
        filename = current_folder + "\\AnnualExpenseData\\" + str(year_search) + "MonthlyExpenses.csv"
        if not(os.path.exists(filename)):
            print("The year entered doesn't have data. Being directed to the main menu.")
            return 0

    # TODO ASK PROF HOW TO GET MINTH DATA W/O YEAR DATA
    if not(month_input == "None"):
        month_search = month_input.group(1)

    if not(categ_input == "None"):
        categ_search = categ_input.group(1)

    if not(name_input == "None"):
        name_search = name_input.group(1)

    if not(due_input == "None"):
        due_search = due_input.group(1)

    if not(date_input == "None"):
        date_search = date_input.group(1)

    if not(paid_input == "None"):
        paid_search = paid_input.group(1)

    if not(pay_due_input == "None"):
        pay_due_search = pay_due_input.group(1)

    if not(method_input == "None"):
        method_search = method_input.group(1)




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

