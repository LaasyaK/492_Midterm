import os
import re
import csv
from OtherFunctions import search_validity

# getting the Header, expense_category, names, and payment_method info from DefaultsRecord
with open("DefaultsRecord.txt", 'r', newline='') as defaults:
    content = defaults.read()
    groups = re.findall(r'(\[.*?\])', content)
    Header = groups[0]
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

    # while loop until user enters valid search criteria
    not_valid = True
    while not_valid:

        # ask user for search criteria in a format
        print("Type in what search criteria you want to search for by typing Field:Data, Field:Data, Field:Data, etc.")
        print("For example: Year:2020, Month:May, Expense_Category:Utility, Payment_Method:Check (make sure if field "
              "has 2 words put an '_' between the words, capitalize field and data entries, and add a ',' to every new"
              " field entry, or type 'main' to return to the main menu.)")
        search_crit = input("Type here: ")

        # check if user input is main
        if search_crit == "main":
            return 0

        # check if input is valid
        elif (search_validity(search_crit)) == "valid":
            not_valid = False

    # check if year is entered
    year_input = re.search(r"Year:(.*?)(?=,)", search_crit)
    if not(year_input == "None"):
        year_search = year_input.group(1)
        current_folder = os.path.dirname(os.path.abspath(__file__))
        filename = current_folder + "\\AnnualExpenseData\\" + str(year_search) + "MonthlyExpenses.csv"

        # data for that year doesn't exist
        if not(os.path.exists(filename)):
            print("The year entered doesn't have data, so data will be printed. Being directed to the main menu.")
            return 0

        # data for that year exists
        else:

            # reading all the data from that year in 2D Array
            file_2d_array = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    file_2d_array.append(row)

            # based on rest criteria, pick out cols and data




        # put into another 2D array, check if more than 10, slowly print 10 at a time
        # index them and print them out
        # ask for modifying w/ index # or going to main menu
        # ask which column needs to be modified w/ indexing cols
        # to delete a row of info and add a new row of info at the BOTTOM







    # year is not entered
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


