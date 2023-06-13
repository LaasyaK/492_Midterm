import re
import datetime
import calendar


# # getting the Header, Expense_Category, names, and payment_method info from DefaultsRecord
# def get_from_defaults():
#     with open("DefaultsRecord.txt", 'r', newline='') as defaults:
#         content = defaults.read()
#         groups = re.findall(r'(\[.*?\])', content)
#         Header = groups[0]
#         Header = eval(Header)
#         Payment_Method = groups[1]
#         Payment_Method = eval(Payment_Method)
#         groups = re.findall(r'({.*?})', content)
#         Expense_Dict = groups[0]
#         Expense_Dict = eval(Expense_Dict)
#         Expense_Category = list(Expense_Dict.keys())
#         Expense_Name = list(Expense_Dict.values())


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



# make func to check validity
def search_validity(search_crit):
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

    #  *** checking year validity ***
    # checking if year is given
    if not (year_input == "None"):
        year_search = year_input.group(1)

        # checking is year given is within bounds or is a number
        try:
            if int(year_search) < 1980 or int(year_search) > datetime.date.today().year:
                print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")
                return 0
        except ValueError:
            print("Can't find data before 1980 or after the current year or an invalid year, try again.\n")
            return 0

    #  *** checking month validity ***
    # checking if month is given
    if not (month_input == "None"):
        month_search = month_input.group(1)

        # checking if month number given is valid and a number
        try:
            if not(int(month_search) in range(1, 13)):
                print("That is not a valid month number or an invalid number, try again.\n")
                return 0
        except ValueError:
            print("That is not a valid month number or an invalid number, try again.\n")
            return 0

    #  *** checking category validity ***
    # checking if month is given
    if not (categ_input == "None"):
        categ_search = categ_input.group(1)

        # checking if category given is in default categories
        if not(categ_search in Expense_Category):
            print("That category is not one of the default categories, try again.\n")
            return 0

    #  *** checking name validity ***
    # checking if name is given
    if not (name_input == "None"):
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

    #  *** checking amount due validity ***
    # checking if amount due is given
    if not (due_input == "None"):
        due_search = due_input.group(1)

        # checking if amount due given is a float
        try:
            due_search = float(due_search)
        except ValueError:
            print("Amount Due can't be any input other than a number or decimal number, try again.\n")
            return 0

    #  *** checking due date validity ***
    # checking if due date is given
    if not (date_input == "None"):
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
            elif int(year) < 1980 or int(year) > 3050:
                print("Due Date can't be an invalid date or year be before 1980, try again.\n")
            elif int(day) > int(month_range[1]+1) or int(day) < 0:
                print("Due Date can't be an invalid date, try again.\n")
        except ValueError:
            print("Due Date can't be an invalid date, try again.\n")
        except TypeError:
            print("Due Date can't be an invalid date, try again.\n")

    #  *** checking amount paid validity ***
    # checking if amount paid is given
    if not (paid_input == "None"):
        paid_search = paid_input.group(1)

        # checking if amount paid given is a float
        try:
            paid_search = float(paid_search)
        except ValueError:
            print("Amount Paid can't be any input other than a number or decimal number, try again.\n")
            return 0

    #  *** checking payment date validity ***
    # checking if payment date is given
    if not (pay_due_input == "None"):
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
            elif int(year) < 1980 or int(year) > 3050:
                print("Payment Date can't be an invalid date or year be before 1980, try again.\n")
            elif int(day) > int(month_range[1] + 1) or int(day) < 0:
                print("Payment Date can't be an invalid date, try again.\n")
        except ValueError:
            print("Payment Date can't be an invalid date, try again.\n")
        except TypeError:
            print("Payment Date can't be an invalid date, try again.\n")

    #  *** checking payment date validity ***
    # checking if payment date is given
    if not (method_input == "None"):
        method_search = method_input.group(1)

        # checking if method given is in default methods
        if not (method_search in Payment_Method):
            print("That Payment Method is not one of the default methods, try again.\n")
            return 0

    # if goes through all checks, return valid
    return "valid"