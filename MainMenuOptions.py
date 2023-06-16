import datetime
import calendar
import re
import csv
import os
from OtherFunctions import search_validity
from OtherFunctions import date_validity



with open("DefaultsRecord.txt", 'r', newline='') as defaults:
    content = defaults.read()
    groups = re.findall(r'(\[.*?\])', content)
    Header = groups[0]
    Header = eval(Header)
    Payment_Method = groups[1]
    Payment_Method = eval(Payment_Method)
    groups = re.findall(r'({.*?})', content)
    Expense_Dict = groups[0]
    Expense_Dict = eval(Expense_Dict)
    Expense_Category = list(Expense_Dict.keys())
    Expense_Name = list(Expense_Dict.values())


# ------------------------------------------- Option (a) Adding a new expense ------------------------------------------

# adds a new expense row to any existing year datasheet or new datasheet            # *** DONE ***
def add_new_expense():
    print("\nAdd a expense Function __________________________________________________________________________________")

    # get and validate year
    not_valid = True
    while not_valid:
        year_change = input("\nWhat year do you want to add the expense to? (or type 'main' to return to the main "
                            "menu.) : ")
        if year_change == "main":
            return 0
        try:
            if int(year_change) < 1980 or int(year_change) > (datetime.date.today().year):
                print("Can't input data before 1980 and after the current year or an invalid year, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input data before 1980 and after the current year or an invalid year, try again.\n")

    # get and validate month
    not_valid = True
    while not_valid:
        month_change = input("\nWhat month do you want to add the expense to? (no abbreviations and must capitalize first"
                             " letter of the month or type 'main' to return to the main menu.) : ")
        if month_change == "main":
            return 0
        for month in range(0, 12):
            if month_change == calendar.month_name[month]:
                not_valid = False
                break
        if not_valid:
            print("Can't input an invalid month name, try again.\n")

    # user chooses Expense_Category from option menu
    not_valid = True
    while not_valid:

        # printing the menu
        print("You will be shown a menu of the available expense categories.")
        for categ in range(0, len(Expense_Category)):
            print(str(categ) + "  " + str(Expense_Category[categ]))

        # getting the user option
        categ_change_num = input("\nWhich expense category do you want to add the expense to? (type in the number "
                                 "associated or type 'main' to return to the main menu.) : ")
        if categ_change_num == "main":
            return 0
        try:
            if not (int(categ_change_num) in range(0, len(Expense_Category))):
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")
    categ_change = Expense_Category[int(categ_change_num)]

    # user chooses Expense_Name from option menu
    not_valid = True
    while not_valid:

        # printing the menu
        print("\nYou will be shown a menu of the available expense names.")
        categ_change_num = int(categ_change_num)
        for name in range(0, len(Expense_Name[categ_change_num])):
            print(str(name) + "  " + str(Expense_Name[categ_change_num][name]))

        # getting the user option
        name_change = input("Which expense name do you want to add the expense to? (type in the number associated or "
                            "type 'main' to return to the main menu.) : ")
        if name_change == "main":
            return 0
        try:
            if int(name_change) == 0:
                not_valid = False
            if not (int(name_change) in range(len(Expense_Name[categ_change_num][int(name_change)]))):
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")
        except IndexError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")
    name_change = Expense_Name[categ_change_num][int(name_change)]

    # user enters amount due
    not_valid = True
    while not_valid:
        due_change = input("\nHow much is due for the expense? (or type 'main' to return to the main menu.) : ")
        if due_change == "main":
            return 0
        try:
            if float(due_change) < 0:
                print("Can't input a non-number or a negative number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input a non-number or a negative number, try again.\n")
    due_change = round(float(due_change), 2)

    # user may or may not enter due date
    not_valid = True
    while not_valid:
        date_change = input("\nWhat due date do you want to change the expense to? (enter in mm/dd/yyyy format, press enter"
                            " to skip, or type 'main' to return to the main menu.) : ")
        if date_change == "main":
            return 0
        elif date_change == "":
            not_valid = False
        elif date_validity(date_change) == date_change:
            not_valid = False
        else:
            print("Can't enter an invalid date or an unreasonable date, try again.")

    # user may or may not enter amount paid
    not_valid = True
    while not_valid:
        paid_change = input("\nWhat amount do you want to enter for amount paid? (press enter to skip or type 'main' "
                            "to return to the main menu.) : ")
        if paid_change == "main":
            return 0
        try:
            if float(paid_change) < 0:
                print("Can't input a non-number or a negative number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input a non-number or a negative number, try again.\n")
    paid_change = round(float(paid_change), 2)

    # user may or may not enter payment date
    not_valid = True
    while not_valid:
        pay_date_change = input("\nWhat payment date do you want add to the expense? (enter in mm/dd/yyyy format, press"
                                " enter to skip, or type 'main' to return to the main menu.) : ")
        if pay_date_change == "main":
            return 0
        elif pay_date_change == "":
            not_valid = False
        elif date_validity(pay_date_change) == pay_date_change:
            not_valid = False
        else:
            print("Can't enter an invalid date or an unreasonable date, try again.")

    # user may or may not enter payment method
    not_valid = True
    while not_valid:

        # printing the menu
        print("\nYou will be shown a menu of the available payment methods.")
        for meth in range(0, len(Payment_Method)):
            print(str(meth) + "  " + str(Payment_Method[meth]))

        # getting the user option
        method_change = input(
            "Which payment method do you want to add the expense to? (type in the number associated, press enter to"
            " skip, or type 'main' to return to the main menu.) : ")
        if method_change == "main":
            return 0
        elif method_change == "":
            not_valid = False
        else:
            try:
                if not (int(method_change) in range(0, len(Payment_Method))):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            method_change = Expense_Category[int(method_change)]

    # double check all info and adding info to file
    print("\nThis will be added to the the " + year_change + " data sheet." )
    print("Month: "+month_change)
    print("Expense_Category: "+categ_change)
    print("Expense_Name: "+name_change)
    print("Amount_Due: "+str(due_change))
    print("Due_Date: "+str(date_change))
    print("Amount_Paid: "+str(paid_change))
    print("Payment_Date: "+str(pay_date_change))
    print("Payment_Method: "+str(method_change))
    not_valid = True
    while not_valid:
        response = input("Do you want to add this expense? (type 'y', 'n', or 'main' to return to the main menu.) : ")
        if response == "main":
            return 0
        elif response == "y":
            current_folder = os.path.dirname(os.path.abspath(__file__))
            filename = current_folder + "\\AnnualExpenseData\\" + str(year_change) + "MonthlyExpenses.csv"
            row = []
            row.append(str(year_change))
            row.append(str(month_change))
            row.append(str(categ_change))
            row.append(str(name_change))
            row.append(str(date_change))
            row.append(str(paid_change))
            row.append(str(pay_date_change))
            row.append(str(method_change))
            if (os.path.exists(filename)):
                with open(filename, 'a', newline='') as file:
                    add = csv.writer(file)
                    add.writerow(row)
                    not_valid = False
            else:
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(Header)
                    writer.writerow(row)
                    not_valid = False
            print("Expense added. Being directed to the main menu.")
        elif response == "n":
            print("No expense added. Being directed to the main menu.")
            not_valid = False
        else:
            print("Can't enter characters other than 'y' or 'n', try again.")


# ------------------------------------ Option (b) Searching and modifying an expense -----------------------------------

# searches and modifies an expense in a datasheet                               # *** DONE ***
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

        elif search_crit == "":
            print("No Search Criteria is inputted, returning to Main Menu.")
            return 0

        # check if input is valid
        elif not((search_validity(search_crit)) == 0):
            not_valid = False

    # finds the criteria that is being searched and put into list
    criteria = search_validity(search_crit)
    print("This is the search criteria that will be searched for: ")
    print(criteria)

    # *** check if year is entered in str ***
    year_input = re.search(r"Year:(.*?)(?=,)", search_crit)
    year_input2 = re.search(r"Year:(.*)", search_crit)
    if year_input or year_input2:
        if year_input:
            year_search = year_input.group(1)
        else:
            year_search = year_input2.group(1)
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
                            print_resume = input("\nMore than 10 matching expense entries, print ('y', 'n', or 'main' to "
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

            # ask user which record to change
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
                    elif not(int(modifying_index) in range(index)):
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
                validity_check = str(Header[int(modifying_field)]) + ":" + str(value_change)
                if value_change == "main":
                    return 0

                # checking the validity of the value
                elif (search_validity(validity_check)) == 0:
                    print("")
                else:
                    not_valid = False

            # copy existing record to new list and modify new list to have change in field
            new_row = for_printing[int(modifying_index)][:]
            new_row[int(modifying_field)] = str(value_change)

            # find index the record exists in the file_2d_array
            for line_num in range(len(file_2d_array)):
                if file_2d_array[line_num] == for_printing[int(modifying_index)]:
                    index_whole = line_num

            # delete the row that is being modified
            if (int(index_whole)) < len(file_2d_array):
                del file_2d_array[(int(index_whole))]

            # Write the updated data back to the CSV file
            with open(filename, 'w', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerows(file_2d_array)
                csv_writer.writerow(new_row)
            print("Record is Modified.")

    # *** year is not entered ***
    else:

        # find how many files in the AnnualExpenseData folder
        current_folder = os.path.dirname(os.path.abspath(__file__))
        filename = current_folder + "\\AnnualExpenseData"
        years_files = os.listdir(filename)
        years_files_count = len(os.listdir(filename))

        # add all the data from all the files to a 2D array
        files_2d_array = []

        # open each file and put all the data into files_2d_array
        for file in years_files:
            filename = current_folder + "\\AnnualExpenseData\\" + str(file)
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    files_2d_array.append(row)

        # storing the col numbers the criteria exists in a list
        criteria_exist = []
        for i in range(len(criteria)):
            if not (criteria[i] == ""):
                criteria_exist.append(i)

        # appending what matches search criteria to another list
        for_printing = []

        # for loop to check every row in file_2d_array
        for rows in range(len(files_2d_array)):
            match = True

            # for loop to check search criteria contents in a row
            for num in criteria_exist:
                if not (criteria[num] == files_2d_array[rows][num]):
                    match = False
            if match:
                for_printing.append(files_2d_array[rows])

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
                    if ((index + 1) % 10) == 0:
                        print_resume = input(
                            "More than 10 matching expense entries, print ('y', 'n', or 'main' to "
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

        # ask user which record to change
        print("\n")
        not_valid = True
        while not_valid:
            modifying_index = input(
                "What record do you want to modify? (type in the number to the left of it "
                "or type 'main' to return to the main menu.) : ")
            if modifying_index == "main":
                return 0
            try:
                if not (int(modifying_index) in range(0, len(for_printing))):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                elif not (int(modifying_index) in range(index)):
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
                if not (int(modifying_field) in range(0, len(Header))):
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
            validity_check = str(Header[int(modifying_field)]) + ":" + str(value_change)
            if value_change == "main":
                return 0

            # checking the validity of the value
            elif (search_validity(validity_check)) == 0:
                print("")
            else:
                not_valid = False

        # copy existing record to new list and modify new list to have change in field
        new_row = for_printing[int(modifying_index)][:]
        new_row[int(modifying_field)] = str(value_change)

        # make new list of which year file the record is being held
        current_year_data = []
        year = new_row[0]
        filename = current_folder + "\\AnnualExpenseData\\" + str(year) + "MonthlyExpenses.csv"
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                current_year_data.append(row)

        # find index of where the record exists in current_year_data
        for line_num in range(len(current_year_data)):
            if current_year_data[line_num] == for_printing[int(modifying_index)]:
                index_whole = line_num

        # delete the row that is being modified
        if (int(index_whole)) < len(current_year_data):
            del current_year_data[(int(index_whole))]

        # Write the updated data back to the CSV file
        with open(filename, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(current_year_data)
            csv_writer.writerow(new_row)
        print("Record is Modified.")


# ---------------------------- Option (c) Adding a expense category, name, or payment method ---------------------------

# adding an expense category, expense name, or payment method to the defaults           # *** DONE ***
def add_categ_name_method():
    print("\nAdd an Expense_Category, Expense_Name, or Payment Method Function _______________________________________")

    no_error = True
    while no_error:
        # print a menu of the option to add
        print("You will be shown a menu of adding options.")
        print("0  Add a new Expense_Category and associated new Expense_Name")
        print("1  Add a new Expense_Name to an existing Expense_Category")
        print("2  Add a new Payment_Method")

        # ask for user input
        to_change = input("Which option do you want to add to? (type in the number associated or type 'main' to return"
                          " to the main menu.) : ")

        # based on input alot variables w/ info
        if to_change == "main":
            return 0

        # typing in a new category and name or typing main
        elif to_change == "0":
            print("\nThese are the current Expense_Categories: [Expense_Names] in a dictionary: ")
            print(Expense_Dict)
            categ_add = input("What Category do you want to add? (or type 'main' to return to the main menu.) : ")
            if categ_add == "main":
                return 0
            name_add = input("What Name do you want to add to that Category? (or type 'main' to return to the main "
                             "menu.) : ")
            if name_add == "main":
                return 0
            Expense_Dict.update({categ_add: [name_add]})
            print("Expense category and name added. Being directed to the main menu.")
            no_error = False

        # typing a new name for an existing category or typing main
        elif to_change == "1":
            not_valid = True
            while not_valid:

                # asking which category first
                print("\nThese are the current Expense_Categories: ")
                for elem in range(len(Expense_Category)):
                    print(str(elem) + "  " + str(Expense_Category[elem]))
                categ = input("Which Expense Category do you want to a new Expense Name to? (type in the number "
                              "associated or type 'main' to return to the main menu.) : ")
                if categ == "main":
                    return 0
                try:
                    if not (int(categ) in range(0, len(Expense_Category))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

                # printing existing names in that category
                print("These are the existing names in that category. : ")
                print(Expense_Name[int(categ)])

                # asking for name
                name = input("What Name do you want to add to that Category? (or type 'main' to return to the main "
                             "menu.) : ")
                if name == "main":
                    return 0
                temp_list = Expense_Name[int(categ)] + [name]
                Expense_Dict[Expense_Category[int(categ)]] = temp_list
                print("Expense name added. Being directed to the main menu.")
                not_valid = False
                no_error = False

        # adding a payment method
        elif to_change == "2":
            print("\nThese are the current Payment_Methods: ")
            print(Payment_Method)
            method_add = input("What Payment Method do you want to add? (or type 'main' to return to the main menu.) : ")
            if method_add == "main":
                return 0
            Payment_Method.append(method_add)
            print("Payment method added. Being directed to the main menu.")
            no_error = False

        else:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # put the changed variables into the DefaultsRecord
        with open("DefaultsRecord.txt", 'w', newline='') as writer:
            writer.write("Header = " + str(Header) + "\n")
            writer.write("Payment_Method = " + str(Payment_Method) + "\n")
            writer.write("Expense_Dict = " + str(Expense_Dict) + "\n")


# ------------------------------- Option (d) Import Expense Data from a csv or text file -------------------------------