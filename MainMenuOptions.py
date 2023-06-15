# TODO 4 OF THEM


import datetime
import calendar
import re
import csv
import os



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

# adds a new expense row to any existing year datasheet or new datasheet            # TODO 4 OF THEM
def add_new_expense():
    print("\nAdd a expense Function __________________________________________________________________________________")

    # get and validate year
    not_valid = True
    while not_valid:
        year_change = input("What year do you want to add the expense to? (or type 'main' to return to the main "
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
        month_change = input("What month do you want to add the expense to? (no abbreviations and must capitalize first"
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
        categ_change_num = input("Which expense category do you want to add the expense to? (type in the number "
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

    # user chooses Expense_Name from option menu        # TODO FOR CCBILL IT DONT WORK
    not_valid = True
    while not_valid:

        # printing the menu
        print("You will be shown a menu of the available expense names.")
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
                break
            if not (int(name_change) in range(0, len(Expense_Name[categ_change_num][int(name_change)]))):
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")
    name_change = Expense_Name[categ_change_num][int(name_change)]

    # user enters amount due
    not_valid = True
    while not_valid:
        due_change = input("How much is due for the expense? (or type 'main' to return to the main menu.) : ")
        if year_change == "main":
            return 0
        try:
            if float(due_change) < 0:
                print("Can't input a non-number or a negative number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input a non-number or a negative number, try again.\n")
    due_change = round(float(due_change), 2)

    # user may or may not enter due date    # TODO THIS PART CRASHES IF NIT INOUT CORRECTLY, NEED TO CATCH ERROR
    not_valid = True
    date_change = input("What due date do you want to change the expense to? (enter in mm/dd/yyyy format, press enter"
                        " to skip, or type 'main' to return to the main menu.) : ")
    if year_change == "main":
        return 0
    elif date_change == "":
        not_valid = False
    else:
        try:
            while not_valid:
                dates = re.search(r'(\d+)\/', date_change)
                month = dates.group(1)
                dates = re.search(r'\/(\d+)\/', date_change)
                day = dates.group(1)
                dates = re.findall(r'\/(\d+)', date_change)
                year = dates[1]
                month_range = calendar.monthrange(int(year), int(month))
                if int(month) > 12 or int(month) < 1:
                    print("Can't enter an invalid date or an unreasonable date, try again.\n")
                elif int(year) < 1980 or int(year) > 3050:
                    print("Can't enter an invalid date or an unreasonable date, try again.\n")
                elif int(day) > int(month_range[1]+1) or int(day) < 0:
                    print("Can't enter an invalid date or an unreasonable date, try again.\n")
                else:
                    not_valid = False
        except ValueError:
                print("Can't enter an invalid date or an unreasonable date, try again.\n")
        except TypeError:
                print("Can't enter an invalid date or an unreasonable date, try again.\n")
        date_change = str(month) + "/" + str(day) + "/" + str(year)

    # user may or may not enter amount paid     # TODO ERROR DIDNT LET ME PUT IN #
    not_valid = True
    while not_valid:
        paid_change = input("What amount do you want to enter for amount paid? (press enter to skip or type 'main' to "
                            "return to the main menu.) : ")
        if year_change == "main":
            return 0
        try:
            if paid_change == "":
                paid_change = ""
                not_valid = False
                break
            elif paid_change < 0:
                print("Can't input a non-number or a negative number, try again.\n")
            elif type(paid_change) == float or type(paid_change) == int:
                not_valid = False
                paid_change = round(paid_change, 2)
                break
            else:
                print("Can't input a non-number or a negative number, try again.\n")
        except TypeError:
            print("Can't input a non-number or a negative number, try again.\n")

    # user may or may not enter payment date        # TODO THIS PART CRASHES IF NIT INOUT CORRECTLY, NEED TO CATCH ERROR
    not_valid = True
    while not_valid:
        pay_date_change = input("What payment date do you want add to the expense? (enter in mm/dd/yyyy format, press"
                                " enter to skip, or type 'main' to return to the main menu.) : ")
        if year_change == "main":
            return 0
        elif pay_date_change == "":
            not_valid = False
        else:
            try:
                dates2 = re.search(r'(\d+)\/', pay_date_change)
                month2 = dates2.group(1)
                dates2 = re.search(r'\/(\d+)\/', pay_date_change)
                day2 = dates2.group(1)
                dates2 = re.findall(r'\/(\d+)', pay_date_change)
                year2 = dates2[1]
                month_range2 = calendar.monthrange(int(year2), int(month2))
                if int(month2) > 12 or int(month2) < 1:
                    print("Can't enter an invalid date or an unreasonable date, try again.\n")
                elif int(year2) < 1980 or int(year2) > 3050:
                    print("Can't enter an invalid date or an unreasonable date, try again.\n")
                elif int(day2) > int(month_range2[1]) or int(day2) < 0:
                    print("Can't enter an invalid date or an unreasonable date, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't enter an invalid date or an unreasonable date, try again.\n")
            except TypeError:
                print("Can't enter an invalid date or an unreasonable date, try again.\n")
            pay_date_change = str(month2) + "/" + str(day2) + "/" + str(year2)

    # user may or may not enter payment method
    not_valid = True
    while not_valid:

        # printing the menu
        print("You will be shown a menu of the available payment methods.")
        for meth in range(0, len(Payment_Method)):
            print(str(meth) + "  " + str(Payment_Method[meth]))

        # getting the user option
        method_change = input(
            "Which payment method do you want to add the expense to? (type in the number associated, press enter to"
            " skip, or type 'main' to return to the main menu.) : ")
        if year_change == "main":
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
        if year_change == "main":
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