"""
Author: Laasya Kallepalli
Date: 6/20/2023
Purpose: Holds the other functions that are used to help run the main menu functions
Functions: search_validity, date_validity, search_all_expense_data
"""

import re
import datetime
import calendar
import os
import csv
import platform



# getting the header, expense_category, names, and payment_method info from DefaultsRecord
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

operating_system = platform.system()


def search_validity(search_crit):
    """
    Author: Laasya Kallepalli
    Date: 6/20/2023
    Purpose: Check validity of users inputted search criteria and throws errors telling user what is wrong
    Input(s): Takes the string of the search criteria
    Output(s): Returns the criteria without the fields if all the checks are passed
    """
    criteria = []

    # getting search object from user input
    year_input = re.search(r"Year:(.*?)(?=,)", search_crit)
    year_input2 = re.search(r"Year:(.*)", search_crit)
    month_input = re.search(r"Month:(.*?)(?=,)", search_crit)
    month_input2 = re.search(r"Month:(.*)", search_crit)
    categ_input = re.search(r"Expense_Category:(.*?)(?=,)", search_crit)
    categ_input2 = re.search(r"Expense_Category:(.*)", search_crit)
    name_input = re.search(r"Expense_Name:(.*?)(?=,)", search_crit)
    name_input2 = re.search(r"Expense_Name:(.*)", search_crit)
    due_input = re.search(r"Amount_Due:(.*?)(?=,)", search_crit)
    due_input2 = re.search(r"Amount_Due:(.*)", search_crit)
    date_input = re.search(r"Due_Date:(.*?)(?=,)", search_crit)
    date_input2 = re.search(r"Due_Date:(.*)", search_crit)
    paid_input = re.search(r"Amount_Paid:(.*?)(?=,)", search_crit)
    paid_input2 = re.search(r"Amount_Paid:(.*)", search_crit)
    pay_due_input = re.search(r"Payment_Date:(.*?)(?=,)", search_crit)
    pay_due_input2 = re.search(r"Payment_Date:(.*)", search_crit)
    method_input = re.search(r"Payment_Method:(.*?)(?=,)", search_crit)
    method_input2 = re.search(r"Payment_Method:(.*)", search_crit)


    #  *** checking year validity ***
    # checking if year is given within string with ,s
    if year_input:
        year_search = year_input.group(1)

        # checking is year given is within bounds or is a number
        try:
            if int(year_search) < 1980 or int(year_search) > datetime.date.today().year:
                print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")
                return 0
        except ValueError:
            print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")
            return 0
        criteria.append(year_search)

    # checking if year is given itself or at the end of str
    elif year_input2:
        year_search = year_input2.group(1)

        # checking is year given is within bounds or is a number
        try:
            if int(year_search) < 1980 or int(year_search) > datetime.date.today().year:
                print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")
                return 0

        except ValueError:
            print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")
            return 0
        criteria.append(year_search)

    else:
        criteria.append("")


    #  *** checking month validity ***
    # checking if month is given in str w/ ,s
    if month_input:
        month_search = month_input.group(1)

        # checking if month str given is valid
        month_right = False
        for month in range(1, 13):
            if month_search == calendar.month_name[month]:
                month_right = True
        if not(month_right):
            print("That month is not a valid month, try again.\n")
            return 0
        criteria.append(month_search)

    # checking if month is given at end of str
    elif month_input2:
        month_search = month_input2.group(1)

        # checking if month str given is valid
        month_right = False
        for month in range(1, 13):
            if month_search == calendar.month_name[month]:
                month_right = True
        if not (month_right):
            print("That month is not a valid month, try again.\n")
            return 0
        criteria.append(month_search)

    else:
        criteria.append("")


    #  *** checking category validity ***
    # checking if month is given in str w/ ,s
    if categ_input:
        categ_search = categ_input.group(1)

        # checking if category given is in default categories
        if not(categ_search in Expense_Category):
            print("That category is not one of the default categories, try again.\n")
            return 0
        criteria.append(categ_search)

    # checking if month is given at end of str
    elif categ_input2:
        categ_search = categ_input2.group(1)

        # checking if category given is in default categories
        if not (categ_search in Expense_Category):
            print("That category is not one of the default categories, try again.\n")
            return 0
        criteria.append(categ_search)

    else:
        criteria.append("")


    #  *** checking name validity ***
    # checking if name is given in str w/,s
    if name_input:
        name_search = name_input.group(1)

        # checking if name given is in default names
        name_exists = False
        for grouping in Expense_Name:
            if name_search in grouping:
                name_exists = True
                break
        if not(name_exists):
            print("That name is not one of the default names, try again.\n")
            return 0
        criteria.append(name_search)

    # checking if name is given in str at end
    elif name_input2:
        name_search = name_input2.group(1)

        # checking if name given is in default names
        name_exists = False
        for grouping in Expense_Name:
            if name_search in grouping:
                name_exists = True
                break
        if not (name_exists):
            print("That name is not one of the default names, try again.\n")
            return 0
        criteria.append(name_search)

    else:
        criteria.append("")


    #  *** checking amount due validity ***
    # checking if amount due is given in str w/ ,
    if due_input:
        due_search = due_input.group(1)

        # checking if amount due given is a float
        try:
            due_search = float(due_search)
        except ValueError:
            print("Amount Due can't be any input other than a number or decimal number, try again.\n")
            return 0
        criteria.append(due_search)

    # checking if amount due is given at end of str
    elif due_input2:
        due_search = due_input2.group(1)

        # checking if amount due given is a float
        try:
            due_search = float(due_search)
        except ValueError:
            print("Amount Due can't be any input other than a number or decimal number, try again.\n")
            return 0
        criteria.append(due_search)

    else:
        criteria.append("")


    #  *** checking due date validity ***
    # checking if due date is given in str w/ ,s
    if date_input:
        date_search = date_input.group(1)

        # checking if due date is an actual date
        try:
            dates = re.search(r'(\d+)\/', date_search)
            month = dates.group(1)
            dates = re.search(r'\/(\d+)\/', date_search)
            day = dates.group(1)
            dates = re.findall(r'\/(\d+)', date_search)
            year = dates[1]
            month_range = calendar.monthrange(int(year), int(month))
            if int(month) > 12 or int(month) < 1:
                print("Due Date can't be an invalid date, try again.\n")
                return 0
            elif int(year) < 1980 or int(year) > 3050:
                print("Due Date can't be an invalid date or year be before 1980, try again.\n")
                return 0
            elif int(day) > int(month_range[1]) or int(day) < 0:
                print("Due Date can't be an invalid date, try again.\n")
                return 0
        except ValueError:
            print("Due Date can't be an invalid date, try again.\n")
            return 0
        except TypeError:
            print("Due Date can't be an invalid date, try again.\n")
            return 0
        except AttributeError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        criteria.append(date_search)

    # checking if due date is given at end of str
    elif date_input2:
        date_search = date_input2.group(1)

        # checking if due date is an actual date
        try:
            dates = re.search(r'(\d+)\/', date_search)
            month = dates.group(1)
            dates = re.search(r'\/(\d+)\/', date_search)
            day = dates.group(1)
            dates = re.findall(r'\/(\d+)', date_search)
            year = dates[1]
            month_range = calendar.monthrange(int(year), int(month))
            if int(month) > 12 or int(month) < 1:
                print("Due Date can't be an invalid date, try again.\n")
                return 0
            elif int(year) < 1980 or int(year) > 3050:
                print("Due Date can't be an invalid date or year be before 1980, try again.\n")
                return 0
            elif int(day) > int(month_range[1]) or int(day) < 0:
                print("Due Date can't be an invalid date, try again.\n")
                return 0
        except ValueError:
            print("Due Date can't be an invalid date, try again.\n")
            return 0
        except TypeError:
            print("Due Date can't be an invalid date, try again.\n")
            return 0
        except AttributeError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        criteria.append(date_search)

    else:
        criteria.append("")


    #  *** checking amount paid validity ***
    # checking if amount paid is given in str w/ ,s
    if paid_input:
        paid_search = paid_input.group(1)

        # checking if amount paid given is a float
        try:
            paid_search = float(paid_search)
        except ValueError:
            print("Amount Paid can't be any input other than a number or decimal number, try again.\n")
            return 0
        criteria.append(paid_search)

    # checking if amount paid is given at end of str
    elif paid_input2:
        paid_search = paid_input2.group(1)

        # checking if amount paid given is a float
        try:
            paid_search = float(paid_search)
        except ValueError:
            print("Amount Paid can't be any input other than a number or decimal number, try again.\n")
            return 0
        criteria.append(paid_search)

    else:
        criteria.append("")


    #  *** checking payment date validity ***
    # checking if payment date is given in str w/ ,s
    if pay_due_input:
        pay_due_search = pay_due_input.group(1)

        # checking if payment date is an actual date
        try:
            dates = re.search(r'(\d+)\/', pay_due_search)
            month = dates.group(1)
            dates = re.search(r'\/(\d+)\/', pay_due_search)
            day = dates.group(1)
            dates = re.findall(r'\/(\d+)', pay_due_search)
            year = dates[1]
            month_range = calendar.monthrange(int(year), int(month))
            if int(month) > 12 or int(month) < 1:
                print("Payment Date can't be an invalid date, try again.\n")
                return 0
            elif int(year) < 1980 or int(year) > 3050:
                print("Payment Date can't be an invalid date or year be before 1980, try again.\n")
                return 0
            elif int(day) > int(month_range[1]) or int(day) < 0:
                print("Payment Date can't be an invalid date, try again.\n")
                return 0
        except ValueError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        except TypeError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        except AttributeError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        criteria.append(pay_due_search)

    # checking if payment date is given at end of str
    elif pay_due_input2:
        pay_due_search = pay_due_input2.group(1)

        # checking if payment date is an actual date
        try:
            dates = re.search(r'(\d+)\/', pay_due_search)
            month = dates.group(1)
            dates = re.search(r'\/(\d+)\/', pay_due_search)
            day = dates.group(1)
            dates = re.findall(r'\/(\d+)', pay_due_search)
            year = dates[1]
            month_range = calendar.monthrange(int(year), int(month))
            if int(month) > 12 or int(month) < 1:
                print("Payment Date can't be an invalid date, try again.\n")
                return 0
            elif int(year) < 1980 or int(year) > 3050:
                print("Payment Date can't be an invalid date or year be before 1980, try again.\n")
                return 0
            elif int(day) > int(month_range[1]) or int(day) < 0:
                print("Payment Date can't be an invalid date, try again.\n")
                return 0
        except ValueError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        except TypeError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        except AttributeError:
            print("Payment Date can't be an invalid date, try again.\n")
            return 0
        criteria.append(pay_due_search)

    else:
        criteria.append("")


    #  *** checking payment date validity ***
    # checking if payment date is given in str w/ ,s
    if method_input:
        method_search = method_input.group(1)

        # checking if method given is in default methods
        if not (method_search in Payment_Method):
            print("That Payment Method is not one of the default methods, try again.\n")
            return 0
        criteria.append(method_search)

    # checking if payment date is given at end of str
    elif method_input2:
        method_search = method_input2.group(1)

        # checking if method given is in default methods
        if not (method_search in Payment_Method):
            print("That Payment Method is not one of the default methods, try again.\n")
            return 0
        criteria.append(method_search)

    else:
        criteria.append("")


    # *** if goes through all checks, returns list of search criteria ***
    return criteria


def date_validity(date_input):
    """
    Author: Laasya Kallepalli
    Date: 6/20/2023
    Purpose: Checks validity of an inputed string of a date
    Input(s): Takes the string of a date
    Output(s): Returns the date if all the checks are passed
    """

    # checking if due date is an actual date
    try:
        dates1 = re.search(r'(\d+)\/', date_input)
        dates2 = re.search(r'\/(\d+)\/', date_input)
        dates3 = re.findall(r'\/(\d+)', date_input)
        if dates1 and dates2 and dates3:
            month = dates1.group(1)
            day = dates2.group(1)
            year = dates3[1]
            month_range = calendar.monthrange(int(year), int(month))
            if int(month) > 12 or int(month) < 1:
                return 0
            elif int(year) < 1980 or int(year) > 3050:
                return 0
            elif int(day) > int(month_range[1]) or int(day) < 0:
                return 0
            else:
                return date_input
    except ValueError:
        return 0
    except TypeError:
        return 0
    except AttributeError:
        return 0
    return 0


def search_all_expense_data(search_crit):
    """
    Author: Laasya Kallepalli
    Date: 6/20/2023
    Purpose: Searches all the datasheets available and puts the data into a list
    Input(s): Takes the string of the search criteria
    Output(s): Returns a large 2D list of all the records according to the search criteria
    """

    # finds the criteria that is being searched and put into list
    criteria = search_validity(search_crit)

    # *** check if year is entered in str ***
    year_input = re.search(r"Year:(.*?)(?=,)", search_crit)
    year_input2 = re.search(r"Year:(.*)", search_crit)
    if year_input or year_input2:
        if year_input:
            year_search = year_input.group(1)
        else:
            year_search = year_input2.group(1)
        current_folder = os.path.dirname(os.path.abspath(__file__))
        if operating_system == "Windows":
            filename = current_folder + "\\AnnualExpenseData\\" + str(year_search) + "MonthlyExpenses.csv"
        else:
            filename = current_folder + "/AnnualExpenseData/" + str(year_search) + "MonthlyExpenses.csv"

        # data for that year doesn't exist
        if not (os.path.exists(filename)):
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
            criteria_exist = []
            for i in range(len(criteria)):
                if not (criteria[i] == ""):
                    criteria_exist.append(criteria[i])

            # appending what matches search criteria to another list
            for_printing = []

            # for loop to check every row in file_2d_array
            for rows in range(len(file_2d_array)):
                match = True

                # for loop to check search criteria contents in a row
                for elem in criteria_exist:
                    if not (elem in file_2d_array[rows]):
                        match = False
                if match:
                    for_printing.append(file_2d_array[rows])

            return(for_printing)


    # *** year is not entered ***
    else:

        # find how many files in the AnnualExpenseData folder
        current_folder = os.path.dirname(os.path.abspath(__file__))
        if operating_system == "Windows":
            filename = current_folder + "\\AnnualExpenseData"
        else:
            filename = current_folder + "/AnnualExpenseData"
        years_files = os.listdir(filename)
        years_files_count = len(os.listdir(filename))

        # add all the data from all the files to a 2D array
        files_2d_array = []

        # open each file and put all the data into files_2d_array
        for file in years_files:
            if operating_system == "Windows":
                filename = current_folder + "\\AnnualExpenseData\\" + str(file)
            else:
                filename = current_folder + "/AnnualExpenseData/" + str(file)
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    files_2d_array.append(row)

        # storing the col numbers the criteria exists in a list
        criteria_exist = []
        for i in range(len(criteria)):
            if not (criteria[i] == ""):
                criteria_exist.append(criteria[i])

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

        return (for_printing)
