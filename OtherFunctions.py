import re
import datetime
import calendar



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


# make func to check validity of users inputed search criteria
# that prints errors based on which info is not correct and returns the search criteria in a list
def search_validity(search_crit):                                   # *** DONE ***
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
        for month in range(0, 12):
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
        for month in range(0, 12):
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


# make func to check validity of an inputted year
def date_validity(date_input):

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
    return 0
