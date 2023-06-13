import os
import re
import datetime


# getting the header, expense_category, names, and payment_method info from DefaultsRecord
with open("DefaultsRecord.txt", 'r', newline='') as defaults:
    content = defaults.read()
    groups = re.findall(r'(\[.*?\])', content)
    header = groups[0]
    Payment_Method = groups[1]
    Payment_Method = eval(Payment_Method)
    groups = re.findall(r'({.*?})', content)
    Expense_dict = groups[0]
    Expense_dict = eval(Expense_dict)
    Expense_Category = list(Expense_dict.keys())
    Expense_Name = list(Expense_dict.values())


# searches and modifies an expense in a datasheet
def search_mod_expense():
    print("\nSearch/Modify an expense Function _______________________________________________________________________")

    not_valid = True
    while not_valid:

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

        # getting results w/ year data
        if not(year_input == "None"):
            year_search = year_input.group(1)

            # check for valid year
            try:
                if int(year_search) < 1980 or int(year_search) > (datetime.date.today().year):
                    print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")

                # year data is valid
                else:
                    current_folder = os.path.dirname(os.path.abspath(__file__))
                    filename = current_folder + "\\AnnualExpenseData\\" + str(year_search) + "MonthlyExpenses.csv"
                    if not (os.path.exists(filename)):
                        print("The year entered doesn't have data. Being directed to the main menu.")
                        return 0

                    # year data exists
                    else:
                        print('')
                        # year data exists
                        # take all year data put in 2D array
                        # based on rest criteria, pick out cols and data
                        # put into another 2D array, check if more than 10, slowly print 10 at a time
                        # index them and print them out
                        # ask for modifying w/ index # or going to main menu
                        # ask which column needs to be modified w/ indexing cols
                        # to delete a row of info and add a new row of info at the BOTTOM

                    not_valid = False
            except ValueError:
                print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")
    # -----------------------While end---------------------     # TODO FIGURE OUT WHILE LOOP    # TODO MAKE A SEPARATE FUNCTION TO CHECK VALIDITY OF CRITERIA

        # getting results w/o year data
        else:
            print("")
            # no given year data, need all data from all files in AnnualExpenseData
            # from all the files, read each row as a list
            # with regex, make groups of according to the criteria have
            # make each group a list and put into a 2D array
            # print 2D array with indexes
            # check if more than 10, slowly print 10 at a time
            # index them and print them out
            # ask for modifying w/ index # or going to main menu
            # ask which column needs to be modified w/ indexing cols
            # to delete a row of info and add a new row of info at the BOTTOM

            # checking for month data
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






# ***** Deleting a row from a csv *****
# import csv
#
# # Specify the path to the CSV file
# csv_file_path = 'data.csv'
#
# # Read the contents of the CSV file into a list
# rows = []
# with open(csv_file_path, 'r') as file:
#     csv_reader = csv.reader(file)
#     rows = list(csv_reader)
#
# # Identify the row you want to delete
# row_index_to_delete = 2
#
# # Remove the row from the list
# if row_index_to_delete < len(rows):
#     del rows[row_index_to_delete]
#
# # Write the updated data back to the CSV file
# with open(csv_file_path, 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(rows)
#
# print("Row deleted successfully.")
