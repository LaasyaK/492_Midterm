# TODO NEED TO TEST THIS IS A SAMPLE YEAR DATASHEET


import os
import re
import csv
from OtherFunctions import search_validity



# getting the Header, expense_category, names, and payment_method info from DefaultsRecord
with open("DefaultsRecord.txt", 'r', newline='') as defaults:
    content = defaults.read()
    groups = re.findall(r'(\[.*?\])', content)
    Header = groups[0]
    Header = eval(Header)
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
        print("For example: Year:2020, Month:May, Expense_Category:Utility, Payment_Method:Check ")
        print("Requirements when entering search criteria:")
        print(" - If the field has 2 words, an '_' needs to be between them.")
        print(" - The first letter of the field and data entries need to be capitalized.")
        print(" - Each field and data entry needs to be separated by a ', '.")
        print(" - If a field is misspelled, it will not be included when searching the data.")
        print(" - Or type 'main' to return to the main menu.")
        search_crit = input("Type here: ")

        # check if user input is main
        if search_crit == "main":
            return 0

        # check if input is valid
        elif not((search_validity(search_crit)) == 0):
            not_valid = False

    # finds the criteria that is being searched and put into list
    criteria = search_validity(search_crit)
    print("This is the search criteria that will be searched for: ")
    print(criteria)

    # check if year is entered in str
    year_input = re.search(r"Year:(.*?)(?=,)", search_crit)
    year_input2 = re.search(r"Year:(.*)", search_crit)
    if year_input:
        year_search = year_input.group(1)
        current_folder = os.path.dirname(os.path.abspath(__file__))
        filename = current_folder + "\\AnnualExpenseData\\" + str(year_search) + "MonthlyExpenses.csv"

        # data for that year doesn't exist
        if not(os.path.exists(filename)):
            print("The year entered doesn't have data, so no data will be printed. Being directed to the main menu.")
            return 0

        # data for that year exists
        else:

            # reading all the data from that year in 2D Array
            file_2d_array = []
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    file_2d_array.append(row)

            # storing the col numbers the criteria exists in a list
            criteria_exist =[]
            for i in range(len(criteria)):
                if not(criteria[i] == ""):
                    criteria_exist.append(i)

            # appending what matches search criteria to another list
            for_printing = []

            # for loop to check every row in file_2d_array
            for rows in range(len(file_2d_array)):
                match = True

                # for loop to check search criteria contents in a row
                for num in criteria_exist:
                    if not(criteria[num] == file_2d_array[rows][num]):
                        match = False
                if match:
                    for_printing.append(file_2d_array[rows])

            # printing the search results when less than 10 of them
            if len(for_printing) < 10:
                print("\nPrinting Search Results ...")
                for index in range(0, len(for_printing)):
                    print(str(index) + "  " + str(for_printing[index]))

            # printing the search results when more than 10 of them
            else:
                not_valid = True
                while not_valid:
                    print("\nPrinting Search Results ...")
                    for index in range(0, len(for_printing)):
                        if ((index+1) % 10) == 0:
                            print_resume = input("More than 10 matching expense entries, print ('y', 'n', or 'main' to "
                                                 "return to the main menu): ")
                            if print_resume == "main":
                                return 0
                            elif print_resume == "y":
                                not_valid = False
                                continue
                            elif print_resume == "n":
                                not_valid = False
                                break
                            else:
                                print("Can only input 'y', 'n', or 'main', try again.\n")
                                break
                        print(str(index) + "  " + str(for_printing[index]))

            # ask user which record to change      # TODO WILL ACCEPT INDEX NUM THAT ISN'T PRINTED FROM ABOVE STATEMENT
            print("\n")
            not_valid = True
            while not_valid:
                modifying_index = input("What record do you want to modify? (type in the number to the left of it "
                                        "or type 'main' to return to the main menu.) : ")
                if modifying_index == "main":
                    return 0
                try:
                    if not(int(modifying_index) in range(0, len(for_printing))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

            # asking user which field to change
            print("\n")
            not_valid = True
            while not_valid:
                for elem in range(len(Header)):
                    print(str(elem) + "  " + Header[elem])
                modifying_field = input("What field do you want to modify? (type in the number to the left of it "
                                        "or type 'main' to return to the main menu.) : ")
                if modifying_field == "main":
                    return 0
                try:
                    if not(int(modifying_field) in range(0, len(Header))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")


            # asking what the new value will be
            print("\n")
            not_valid = True
            while not_valid:
                value_change = input("What is the new value (or type 'main' to return to the main menu.) : ")
                if value_change == "main":
                    return 0
            # verify that the value is valid for the field
            # TODO SOMEHOW AFTER GETTING FIELD AND VALUE PUT IT INTO A STR AND PUT IT THROUGH THE CHECK VALIDITY FUNC

            # modify the record w/ info
                # # make a list of previous info of row and modified info
                    # new_row = for_printing[modifying_index][:]
                    # new_row[modifying_field] = value_change
                # # find which index the row is at in file_2d_array
                    # for line_num in range(0, len(file_2d_array)):
                        # if file_2d_array[line_num] == for_printing[modifying_index]
                            # index_whole = line_num
                # # delete the row that is being modifyed
                    # if (int(index_whole)) < len(file_2d_array):
                        # del file_2d_array[(int(index_whole))]
                # # Write the updated data back to the CSV file
                    # with open(filename, 'w', newline='') as f:
                    #     csv_writer = csv.writer(f)
                    #     csv_writer.writerows(file_2d_array)





    # checking if year is entered at end of str
    # elif year_input2:
        # year_search = year_input2.group(1)
        # TODO AFTER THIS LINE CODE FROM IF STATEMENT ABOVE NEEDS TO BE IN THIS CODE BLOCK

    # year is not entered
    # else:
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


search_mod_expense()


