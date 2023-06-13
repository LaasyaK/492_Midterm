# TODO 2 OF THEM

import datetime
import calendar
import re
import csv
import os


# getting the header, expense_category, names, and payment_method info from DefaultsRecord
with open("DefaultsRecord.txt", 'r', newline='') as defaults:
    content = defaults.read()
    groups = re.findall(r'\[(.*?)\]', content)
    header = groups[0]
    header = eval(header)
    Payment_Method = groups[1]
    Payment_Method = eval(Payment_Method)
    groups = re.findall(r'({.*?})', content)
    Expense_dict = groups[0]
    Expense_dict = eval(Expense_dict)
    Expense_category = list(Expense_dict.keys())
    Expense_name = list(Expense_dict.values())


# adds a new expense row to any existing year datasheet or new datasheet # TODO 2 OF THEM
def add_new_expense():
    print("\nAdd a expense Function __________________________________________________________________________________")

    # get and validate year
    not_valid = True
    while not_valid:
        year_change = input("What year do you want to add the expense to? (or type 'main' to return to the main menu.) : ")
        if year_change == "main":
            return 0
        try:
            if int(year_change) < 1980 or int(year_change) > (datetime.date.today().year):
                print("Can't input data before 1980 and after the current year or an invalid year, try again.\n")
            # elif year_change
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

    # user chooses expense_category from option menu
    not_valid = True
    while not_valid:

        # printing the menu
        print("You will be shown a menu of the available expense categories.")
        for categ in range(0, len(Expense_category)):
            print(str(categ) + "  " + str(Expense_category[categ]))

        # getting the user option
        categ_change_num = input("Which expense category do you want to add the expense to? (type in the number associated"
                             " or type 'main' to return to the main menu.) : ")
        if categ_change_num == "main":
            return 0
        try:
            if not (int(categ_change_num) in range(0, len(Expense_category))):
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")
    categ_change = Expense_category[int(categ_change_num)]

    # user chooses expense_name from option menu
    not_valid = True
    while not_valid:

        # printing the menu
        print("You will be shown a menu of the available expense names.")
        categ_change_num = int(categ_change_num)
        for name in range(0, len(Expense_name[categ_change_num])):
            print(str(name) + "  " + str(Expense_name[categ_change_num][name]))

        # getting the user option
        name_change = input("Which expense name do you want to add the expense to? (type in the number associated or "
                            "type 'main' to return to the main menu.) : ")
        if name_change == "main":
            return 0
        try:
            if not (int(name_change) in range(0, len(Expense_name[categ_change_num][name]))):
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")
    name_change = Expense_name[categ_change_num][int(name_change)]

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
                elif int(day) > int(month_range[1]) or int(day) < 0:
                    print("Can't enter an invalid date or an unreasonable date, try again.\n")
                else:
                    not_valid = False
        except ValueError:
                print("Can't enter an invalid date or an unreasonable date, try again.\n")
        except TypeError:
                print("Can't enter an invalid date or an unreasonable date, try again.\n")
        date_change = str(month) + "/" + str(day) + "/" + str(year)

    # user may or may not enter amount paid
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
            method_change = Expense_category[int(method_change)]

    # double check all info and adding info to file
    print("\nThis will be added to the the " + year_change + " data sheet." )
    print("Month: "+month_change)
    print("Expense_category: "+categ_change)
    print("Expense_name: "+name_change)
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
                    writer.writerow(header)
                    writer.writerow(row)
                    not_valid = False
            print("Expense added. Being directed to the main menu.")
        elif response == "n":
            print("No expense added. Being directed to the main menu.")
            not_valid = False
        else:
            print("Can't enter characters other than 'y' or 'n', try again.")