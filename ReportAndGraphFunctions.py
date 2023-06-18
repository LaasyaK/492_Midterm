# TODO 3 OF THEM
# TODO START CODING 3RD GRAPH



import re
import os
import datetime
import csv
import calendar
import numpy
from matplotlib import pyplot as plt
from OtherFunctions import search_all_expense_data



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


# function to run when user wants reports on expenses
def report():
    print("\nMaking a Report__________________________________________________________________________________________")

    # give user menu and asks for option
    not_valid = True
    while not_valid:

        print("\nYou will be shown a menu of options of what report can be made.")
        print("0  Annual Yearly Expense Category or Name amount paid for inputted range of years Report.")
        print("1  Annual Yearly Expense Category and Name amount paid for inputted range of years Report.")
        print("2  Annual Monthly Expenses for a year Report.")
        option_pick = input("Which option do you want to make a report for? (type in the number "
                                 "associated or type 'main' to return to the main menu.) : ")
        if option_pick == "main":
            return 0

        # checking if input is valid
        try:
            if not (int(option_pick) in range(3)):
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")

    # *** making the 1st report ***

    if int(option_pick) == 0:
        print("\nAnnual Yearly Expense Report___________________________________________________________________________")

        # asks user which report type and checks if input is valid
        not_valid = True
        while not_valid:

            print("\n0  csv")
            print("1  txt")
            report_type = input("Which option do you want the report saved as? (type in the number associated or type "
                                "'main' to return to the main menu.) : ")
            if report_type == "main":
                return 0
            try:
                if not (int(report_type) in range(2)):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to pick a specific expense category or name and check if input is valid
        not_valid = True
        while not_valid:

            print("\n0  Expense_Category")
            print("1  Expense_Name")
            categ_name = input("Which option do you want to get data from ? (type in the number associated or type "
                                "'main' to return to the main menu.) : ")
            if categ_name == "main":
                return 0
            try:
                if not (int(categ_name) in range(2)):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        print("\n")
        not_valid = True
        while not_valid:

            # printing and choosing a category
            if int(categ_name) == 0:
                for elem in range(len(Expense_Category)):
                    print(str(elem) + "  " + str(Expense_Category[int(elem)]))
                categ_pick = input("Which option do you want to get data from ? (type in the number associated or type "
                            "'main' to return to the main menu.) : ")
                if categ_pick == "main":
                    return 0
                try:
                    if not (int(categ_pick) in range(len(Expense_Category))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        categ_pick = Expense_Category[int(categ_pick)]
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

            # printing and choosing a name
            else:
                new_Expense_Name = []
                for group in range(0, len(Expense_Name)):
                    for elem in range(len(Expense_Name[group])):
                        new_Expense_Name.append(str(Expense_Name[group][elem]))
                for i in range(len(new_Expense_Name)):
                    print(str(i) + "  " + new_Expense_Name[i])
                name_pick = input("Which option do you want to get data from? (type in the number associated or "
                                          "type 'main' to return to the main menu.) : ")
                if name_pick == "main":
                        return 0
                try:
                    if not (int(name_pick) in range(len(new_Expense_Name))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        name_pick = new_Expense_Name[int(name_pick)]
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to enter year1 in the range of years and validate it
        not_valid = True
        while not_valid:

            year1 = input("\nFor the range of years you want to get data from, what is the start year? (needs to be in format"
                          " yyyy, needs to be a year that has data available, "
                          "or type 'main' to return to the main menu.) :  ")
            if year1 == "main":
                return 0

            # collecting all the years available
            current_folder = os.path.dirname(os.path.abspath(__file__))
            filename = current_folder + "\\AnnualExpenseData"
            years_files = os.listdir(filename)
            years = re.findall(r'(\d.*?)Mon', str(years_files))

            try:
                if int(year1) < 1980 or int(year1) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif not(year1 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to enter year2 in the range of years and validate it
        not_valid = True
        while not_valid:

            year2 = input("\nFor the range of years you want to get data from, what is the end year? (needs to be in "
                          "format yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year2 == "main":
                return 0

            try:
                if int(year2) < 1980 or int(year2) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif int(year2) < int(year1):
                    print("Can't input an end year that is smaller than the start year, try again.\n")
                elif not (year2 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # make list of all years to get data from
        year_num = int(year1)
        year_list = []
        while year_num <= int(year2):
            year_list.append(year_num)
            year_num = year_num + 1

        data_for_report = [['Year', 'Amount_Due', 'Amount_Paid']]

        # for loop of getting data for each year to put in a list
        for year in year_list:

            # putting info from user into a str
            search_criteria = "Year:" + str(year)
            try:
                search_criteria = search_criteria + ", Expense_Category:" + str(categ_pick)
            except UnboundLocalError:
                search_criteria = search_criteria + ", Expense_Name:" + str(name_pick)

            # get all searched results based on criteria and sum up amt paid and due
            to_search = search_all_expense_data(str(search_criteria))

            amt_due_sum = 0
            for each_row in to_search:
                amt_due_sum = amt_due_sum + float(each_row[4])

            amt_paid_sum = 0
            for each_ro in to_search:
                if not(each_ro[6] == ''):
                    amt_paid_sum = amt_paid_sum + float(each_ro[6])

            data_for_report.append([str(year), round(amt_due_sum, 2), round(amt_paid_sum, 2)])

        # add rows of data to csv file in ExpenseReports
        current_folder = os.path.dirname(os.path.abspath(__file__))
        if int(report_type) == 0:
            try:
                filename = current_folder + "\\ExpenseReports\\" + str(categ_pick) + "_Expense_" + str(year1) + "_to_" +\
                           str(year2) + ".csv"
            except UnboundLocalError:
                filename = current_folder + "\\ExpenseReports\\" + str(name_pick) + "_Expense_" + str(year1) + "_to_" +\
                           str(year2) + ".csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data_for_report)

        # add rows of data to txt file in ExpenseReports
        else:
            try:
                filename = current_folder + "\\ExpenseReports\\" + str(categ_pick) + "_Expense_" + str(year1) + "_to_" +\
                           str(year2) + ".txt"
            except UnboundLocalError:
                filename = current_folder + "\\ExpenseReports\\" + str(name_pick) + "_Expense_" + str(year1) + "_to_" +\
                           str(year2) + ".txt"
            with open(filename, 'w') as f:
                for n in data_for_report:
                    f.write(str(n) + "\n")

        print("Report made")


    # making 2nd report     # TODO I DONT UNDERSTAND WHAT THIS REPORT WILL HOLD
        print("")

    # A text or csv report for expenses in for an expense type or category for a year range {year 1 to year 2} or a
        # particular year. 4 columns: expense name, expense category, year, expense. Name the file accordingly.


    elif int(option_pick) == 1:
        print("\nAnnual Yearly Expense with Category and Name_________________________________________________________")

        # asks user which report type and checks if input is valid
        not_valid = True
        while not_valid:

            print("\n0  csv")
            print("1  txt")
            report_type = input("Which option do you want the report saved as? (type in the number associated or type "
                                "'main' to return to the main menu.) : ")
            if report_type == "main":
                return 0
            try:
                if not (int(report_type) in range(2)):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to pick a specific expense category or name and check if input is valid
        not_valid = True
        while not_valid:

            print("\n0  Expense_Category")
            print("1  Expense_Name")
            categ_name = input(
                "Which option do you want to get data from ? (type in the number associated or type "
                "'main' to return to the main menu.) : ")
            if categ_name == "main":
                return 0
            try:
                if not (int(categ_name) in range(2)):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        print("\n")
        not_valid = True
        while not_valid:

            # printing and choosing a category
            if int(categ_name) == 0:
                for elem in range(len(Expense_Category)):
                    print(str(elem) + "  " + str(Expense_Category[int(elem)]))
                categ_pick = input(
                    "Which option do you want to get data from ? (type in the number associated or type "
                    "'main' to return to the main menu.) : ")
                if categ_pick == "main":
                    return 0
                try:
                    if not (int(categ_pick) in range(len(Expense_Category))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        categ_pick = Expense_Category[int(categ_pick)]
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

            # printing and choosing a name
            else:
                new_Expense_Name = []
                for group in range(0, len(Expense_Name)):
                    for elem in range(len(Expense_Name[group])):
                        new_Expense_Name.append(str(Expense_Name[group][elem]))
                for i in range(len(new_Expense_Name)):
                    print(str(i) + "  " + new_Expense_Name[i])
                name_pick = input(
                    "Which option do you want to get data from? (type in the number associated or "
                    "type 'main' to return to the main menu.) : ")
                if name_pick == "main":
                    return 0
                try:
                    if not (int(name_pick) in range(len(new_Expense_Name))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        name_pick = new_Expense_Name[int(name_pick)]
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to enter year1 in the range of years and validate it
        not_valid = True
        while not_valid:

            year1 = input(
                "\nFor the range of years you want to get data from, what is the start year? (needs to be in format"
                " yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year1 == "main":
                return 0

            # collecting all the years available
            current_folder = os.path.dirname(os.path.abspath(__file__))
            filename = current_folder + "\\AnnualExpenseData"
            years_files = os.listdir(filename)
            years = re.findall(r'(\d.*?)Mon', str(years_files))

            try:
                if int(year1) < 1980 or int(year1) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif not (year1 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an invalid year, try again.\n")

        # ask user to enter year2 in the range of years and validate it
        not_valid = True
        while not_valid:

            year2 = input(
                "\nFor the range of years you want to get data from, what is the end year? (needs to be in "
                "format yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year2 == "main":
                return 0

            try:
                if int(year2) < 1980 or int(year2) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif int(year2) < int(year1):
                    print("Can't input an end year that is smaller than the start year, try again.\n")
                elif not (year2 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input an invalid year, try again.\n")

        # make list of all years to get data from
        year_num = int(year1)
        year_list = []
        while year_num <= int(year2):
            year_list.append(year_num)
            year_num = year_num + 1


        # TODO FIGURE OUT WHAT THE REPORTS COLUOMNS ARE
        data_for_report = [['Year', 'Expense_Category', 'Expense_Name', 'Amount_Due', 'Amount_Paid']]

        # for loop of getting data for each year to put in a list
        for year in year_list:

            # putting info from user into a str
            search_criteria = "Year:" + str(year)
            try:
                search_criteria = search_criteria + ", Expense_Category:" + str(categ_pick)
            except UnboundLocalError:
                search_criteria = search_criteria + ", Expense_Name:" + str(name_pick)

            # get all searched results based on criteria and sum up amt paid and due
            to_search = search_all_expense_data(str(search_criteria))

            amt_due_sum = 0
            for each_row in to_search:
                amt_due_sum = amt_due_sum + float(each_row[4])

            amt_paid_sum = 0
            for each_ro in to_search:
                if not (each_ro[6] == ''):
                    amt_paid_sum = amt_paid_sum + float(each_ro[6])

            data_for_report.append([str(year), round(amt_due_sum, 2), round(amt_paid_sum, 2)])




    # *** making the 3rd report ***
    elif int(option_pick) == 2:
        print("\nAnnual Monthly Expenses Report_________________________________________________________________________")

        # asks user which report type and checks if input is valid
        not_valid = True
        while not_valid:

            print("\n0  csv")
            print("1  txt")
            report_type = input("Which option do you want the report saved as? (type in the number associated or type "
                                "'main' to return to the main menu.) : ")
            if report_type == "main":
                return 0
            try:
                if not (int(report_type) in range(2)):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user what year the report will be for and validate it
        not_valid = True
        while not_valid:

            year = input("\nWhat year do you want to get monthly expense for? (needs to be in"
                         " format yyyy, needs to be a year that has data available, "
                         "or type 'main' to return to the main menu.) :  ")
            if year == "main":
                return 0

            # collecting all the years available
            current_folder = os.path.dirname(os.path.abspath(__file__))
            filename = current_folder + "\\AnnualExpenseData"
            years_files = os.listdir(filename)
            years = re.findall(r'(\d.*?)Mon', str(years_files))

            try:
                if int(year) < 1980 or int(year) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif not (year in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # get all the data for the specified year
        search_criteria = "Year:" + year
        to_search = search_all_expense_data(str(search_criteria))

        # for each row sum amount due and paid expenses for each month
        jan1 = 0
        feb1 = 0
        mar1 = 0
        apr1 = 0
        may1 = 0
        jun1 = 0
        jul1 = 0
        aug1 = 0
        sep1 = 0
        oct1 = 0
        nov1 = 0
        dec1 = 0
        jan2 = 0
        feb2 = 0
        mar2 = 0
        apr2 = 0
        may2 = 0
        jun2 = 0
        jul2 = 0
        aug2 = 0
        sep2 = 0
        oct2 = 0
        nov2 = 0
        dec2 = 0
        month_names = calendar.month_name[1:]
        for row_num in range(len(to_search)):
            if to_search[row_num][1] == month_names[0]:
                jan1 = jan1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    jan2 = jan2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[1]:
                feb1 = feb1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    feb2 = feb2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[2]:
                mar1 = mar1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    mar2 = mar2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[3]:
                apr1 = apr1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    apr2 = apr2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[4]:
                may1 = may1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    may2 = may2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[5]:
                jun1 = jun1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    jun2 = jun2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[6]:
                jul1 = jul1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    jul2 = jul2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[7]:
                aug1 = aug1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    aug2 = aug2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[8]:
                sep1 = sep1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    sep2 = sep2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[9]:
                oct1 = oct1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    oct2 = oct2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[10]:
                nov1 = nov1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    nov2 = nov2 + float(to_search[row_num][6])
            elif to_search[row_num][1] == month_names[11]:
                dec1 = dec1 + float(to_search[row_num][4])
                if not (to_search[row_num][6] == ''):
                    dec2 = dec2 + float(to_search[row_num][6])
            else:
                print("Invalid month")
                return 0
        data_for_report = [['Month', 'Amount_Due', 'Amount_Paid'],
                           [month_names[0], round(jan1, 2), round(jan2, 2)],
                           [month_names[1], round(feb1, 2), round(feb2, 2)],
                           [month_names[2], round(mar1, 2), round(mar2, 2)],
                           [month_names[3], round(apr1, 2), round(apr2, 2)],
                           [month_names[4], round(may1, 2), round(may2, 2)],
                           [month_names[5], round(jun1, 2), round(jun2, 2)],
                           [month_names[6], round(jul1, 2), round(jul2, 2)],
                           [month_names[7], round(aug1, 2), round(aug2, 2)],
                           [month_names[8], round(sep1, 2), round(sep2, 2)],
                           [month_names[9], round(oct1, 2), round(oct2, 2)],
                           [month_names[10], round(nov1, 2), round(nov2, 2)],
                           [month_names[11], round(dec1, 2), round(dec2, 2)]]

        # add rows of data to csv file in ExpenseReports
        current_folder = os.path.dirname(os.path.abspath(__file__))
        if int(report_type) == 0:
            filename = current_folder + "\\ExpenseReports\\" + "Monthly_Expenses_for_" + str(year) + ".csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data_for_report)

        # add rows of data to txt file in ExpenseReports
        else:
            filename = current_folder + "\\ExpenseReports\\" + "Monthly_Expenses_for_" + str(year) + ".txt"
            with open(filename, 'w') as f:
                for n in data_for_report:
                    f.write(str(n) + "\n")

        print("Report made")




# function to run when user wants graphs
def graph():
    print("\nMaking a Graph___________________________________________________________________________________________")

    # give user menu and asks for option
    not_valid = True
    while not_valid:

        print("\nYou will be shown a menu of options of what report can be made.")
        print("0  Bar graph for Annual Yearly Expense Category or Name for inputted range of years.")
        print("1  Sub Bar graphs for Annual Yearly Expense Categories or Names for inputted range of years.")
        print("2  Pie Chart for Annual Yearly Expense Categories or Names for a year.")
        print("3  Bar Graph for Annual Monthly Expense each month for a year.")
        option_pick = input("Which option do you want to make a report for? (type in the number "
                            "associated or type 'main' to return to the main menu.) : ")
        if option_pick == "main":
            return 0

        # checking if input is valid
        try:
            if not (int(option_pick) in range(4)):
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")
            else:
                not_valid = False
        except ValueError:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")


    # *** making the 1st report ***         # TODO MAKES THE X-AXIS WITH DECIMALS

    if int(option_pick) == 0:
        print("\nBar graph for Annual Yearly Expense Category or Name___________________________________________________")

        # ask user to pick a specific expense category or name and check if input is valid
        not_valid = True
        while not_valid:

            print("\n0  Expense_Category")
            print("1  Expense_Name")
            categ_name = input("Which option do you want to get data from ? (type in the number associated or type "
                               "'main' to return to the main menu.) : ")
            if categ_name == "main":
                return 0
            try:
                if not (int(categ_name) in range(2)):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        print("\n")
        not_valid = True
        while not_valid:

            # printing and choosing a category
            if int(categ_name) == 0:
                for elem in range(len(Expense_Category)):
                    print(str(elem) + "  " + str(Expense_Category[int(elem)]))
                categ_pick = input("Which option do you want to get data from ? (type in the number associated or type "
                                   "'main' to return to the main menu.) : ")
                if categ_pick == "main":
                    return 0
                try:
                    if not (int(categ_pick) in range(len(Expense_Category))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        categ_pick = Expense_Category[int(categ_pick)]
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

            # printing and choosing a name
            else:
                new_Expense_Name = []
                for group in range(0, len(Expense_Name)):
                    for elem in range(len(Expense_Name[group])):
                        new_Expense_Name.append(str(Expense_Name[group][elem]))
                for i in range(len(new_Expense_Name)):
                    print(str(i) + "  " + new_Expense_Name[i])
                name_pick = input("Which option do you want to get data from? (type in the number associated or "
                                  "type 'main' to return to the main menu.) : ")
                if name_pick == "main":
                    return 0
                try:
                    if not (int(name_pick) in range(len(new_Expense_Name))):
                        print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                    else:
                        name_pick = new_Expense_Name[int(name_pick)]
                        not_valid = False
                except ValueError:
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to enter year1 in the range of years and validate it
        not_valid = True
        while not_valid:

            year1 = input(
                "\nFor the range of years you want to get data from, what is the start year? (needs to be in format"
                " yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year1 == "main":
                return 0

            # collecting all the years available
            current_folder = os.path.dirname(os.path.abspath(__file__))
            filename = current_folder + "\\AnnualExpenseData"
            years_files = os.listdir(filename)
            years = re.findall(r'(\d.*?)Mon', str(years_files))

            try:
                if int(year1) < 1980 or int(year1) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif not (year1 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to enter year2 in the range of years and validate it
        not_valid = True
        while not_valid:

            year2 = input(
                "\nFor the range of years you want to get data from, what is the end year? (needs to be in "
                "format yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year2 == "main":
                return 0

            try:
                if int(year2) < 1980 or int(year2) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif int(year2) < int(year1):
                    print("Can't input an end year that is smaller than the start year, try again.\n")
                elif not (year2 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # make list of all years to get data from
        year_num = int(year1)
        year_list = []
        while year_num <= int(year2):
            year_list.append(year_num)
            year_num = year_num + 1

        # for loop of getting data for each year to put in a list
        x_axis = []
        due_y_axis = []
        paid_y_axis = []
        for year in year_list:

            # putting info from user into a str
            search_criteria = "Year:" + str(year)
            try:
                search_criteria = search_criteria + ", Expense_Category:" + str(categ_pick)
            except UnboundLocalError:
                search_criteria = search_criteria + ", Expense_Name:" + str(name_pick)

            # get all searched results based on criteria and sum up amt paid and due
            to_search = search_all_expense_data(str(search_criteria))

            amt_due_sum = 0
            for each_row in to_search:
                amt_due_sum = amt_due_sum + float(each_row[4])

            amt_paid_sum = 0
            for each_ro in to_search:
                if not (each_ro[6] == ''):
                    amt_paid_sum = amt_paid_sum + float(each_ro[6])

            # add the expense to category or name
            x_axis.append(year)
            due_y_axis.append(round(amt_due_sum, 2))
            paid_y_axis.append(round(amt_paid_sum, 2))

        # add the data to a plot and plot it
        plt.bar(x_axis, due_y_axis)
        plt.bar(x_axis, paid_y_axis)
        try:
            plt.xlabel(str(categ_pick) + " Expense")
            plt.ylabel("Amount of Expense ($)")
            plt.title("The " + str(categ_pick) + " Expense for Each Year")
        except UnboundLocalError:
            plt.xlabel(str(name_pick) + " Expense Year")
            plt.ylabel("Amount of Expense ($)")
            plt.title("The " + str(name_pick) + " Expense for Each Year " + str(year1) + " to " + str(year2))
        plt.legend(["Amount_Due", "Amount_Paid"])
        plt.show()


    # *** making the 2nd report ***     # TODO THIS CODE BLOCK IS RUNNING FOREVER

    elif int(option_pick) == 1:
        print("\nSub Bar graphs for Annual Yearly Expense Categories or Names___________________________________________")

        # ask user to pick a specific expense category or name and check if input is valid
        not_valid = True
        while not_valid:

            print("\n0  Expense_Category")
            print("1  Expense_Name")
            categ_name = input("Which option do you want to get data from ? (type in the number associated or type "
                               "'main' to return to the main menu.) : ")
            if categ_name == "main":
                return 0
            try:
                if not (int(categ_name) in range(2)):
                    print("Can't input an input that isn't the associated 1 digit number, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to enter year1 in the range of years and validate it
        not_valid = True
        while not_valid:

            year1 = input(
                "\nFor the range of years you want to get data from, what is the start year? (needs to be in format"
                " yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year1 == "main":
                return 0

            # collecting all the years available
            current_folder = os.path.dirname(os.path.abspath(__file__))
            filename = current_folder + "\\AnnualExpenseData"
            years_files = os.listdir(filename)
            years = re.findall(r'(\d.*?)Mon', str(years_files))

            try:
                if int(year1) < 1980 or int(year1) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif not (year1 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # ask user to enter year2 in the range of years and validate it
        not_valid = True
        while not_valid:

            year2 = input(
                "\nFor the range of years you want to get data from, what is the end year? (needs to be in "
                "format yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year2 == "main":
                return 0

            try:
                if int(year2) < 1980 or int(year2) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif int(year2) < int(year1):
                    print("Can't input an end year that is smaller than the start year, try again.\n")
                elif not (year2 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # make list of all years to get data from
        year_num = int(year1)
        year_list = []
        while year_num <= int(year2):
            year_list.append(year_num)
            year_num = year_num + 1

        # make x_axis list # of categories or name for all the years
        new_Expense_Name = []
        for group in range(0, len(Expense_Name)):
            for elem in range(len(Expense_Name[group])):
                new_Expense_Name.append(str(Expense_Name[group][elem]))
        divider = []
        for i in range(year_num):
            if categ_name == 0:
                for elem in Expense_Category:
                    divider.append(elem)
            else:
                for elem in new_Expense_Name:
                    divider.append(elem)

        # make the y_axis for each category or name for all the years
        # for each year
        due_y_axis = []
        paid_y_axis = []
        for year in year_list:

            # for each category or name
            word_num = 0
            for word in divider:

                # putting info from user into a str
                search_criteria = "Year:" + str(year)
                if categ_name == 0:
                    search_criteria = search_criteria + ", Expense_Category:" + str(Expense_Category[word_num])
                    word_num = word_num + 1
                    if word_num >= len(Expense_Category):
                        word_num = 0
                else:
                    search_criteria = search_criteria + ", Expense_Name:" + str(new_Expense_Name[word_num])
                    word_num = word_num + 1
                    if word_num >= len(new_Expense_Name):
                        word_num = 0

                # get all searched results based on criteria and sum up amt paid and due
                to_search = search_all_expense_data(str(search_criteria))

                amt_due_sum = 0
                for each_row in to_search:
                    amt_due_sum = amt_due_sum + float(each_row[4])

                amt_paid_sum = 0
                for each_ro in to_search:
                    if not (each_ro[6] == ''):
                        amt_paid_sum = amt_paid_sum + float(each_ro[6])

                # add the expense to category or name
                due_y_axis.append(round(amt_due_sum, 2))
                paid_y_axis.append(round(amt_paid_sum, 2))

        # add the data to a plot and plot it
        plt.bar(divider, due_y_axis)
        plt.bar(divider, paid_y_axis)
        plt.xlabel("Expenses for each Year")
        plt.ylabel("Amount of Expense ($)")
        plt.title("The Expenses according to Type Each Year for " + str(year1) + " to " + str(year2))
        plt.legend(["Amount_Due", "Amount_Paid"])
        plt.show()






    # *** making the 3rd report ***

    elif int(option_pick) == 2:
        print(
            "\nPie Chart for Annual Year Expense Categories or Names___________________________________________________")







    # *** making the 4th report ***                 # *** DONE ***

    elif int(option_pick) == 3:
        print(
            "\nBar Graph for Annual Monthly Expenses in year__________________________________________________________")

        # ask user to enter year to get data from and validate it
        not_valid = True
        while not_valid:

            year1 = input(
                "\nWhat year do you want to get data from? (needs to be in format"
                " yyyy, needs to be a year that has data available, "
                "or type 'main' to return to the main menu.) :  ")
            if year1 == "main":
                return 0

            # collecting all the years available
            current_folder = os.path.dirname(os.path.abspath(__file__))
            filename = current_folder + "\\AnnualExpenseData"
            years_files = os.listdir(filename)
            years = re.findall(r'(\d.*?)Mon', str(years_files))

            try:
                if int(year1) < 1980 or int(year1) > datetime.date.today().year:
                    print("Can't input an invalid year, try again.\n")
                elif not (year1 in years):
                    print("Can't input a year with no data available, try again.\n")
                else:
                    not_valid = False
            except ValueError:
                print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # for loop of getting data for each year to put in a list
        due_y_axis = []
        paid_y_axis = []
        month_names = calendar.month_name[1:]

        # for loop for each month to get expenses for
        for month in month_names:

            search_criteria = "Year:" + str(year1) + ", Month:" + month
            to_search = search_all_expense_data(str(search_criteria))

            amt_due_sum = 0
            for each_row in to_search:
                amt_due_sum = amt_due_sum + float(each_row[4])

            amt_paid_sum = 0
            for each_ro in to_search:
                if not (each_ro[6] == ''):
                    amt_paid_sum = amt_paid_sum + float(each_ro[6])

            # add the expense axises lists
            due_y_axis.append(round(amt_due_sum, 2))
            paid_y_axis.append(round(amt_paid_sum, 2))

        # add the data to a plot and plot it
        x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
        plt.bar(x_axis, due_y_axis)
        plt.bar(x_axis, paid_y_axis)
        plt.xlabel("Months")
        plt.ylabel("Amount of Monthly Expenses ($)")
        plt.title("The Monthly Expenses for " + str(year1))
        plt.legend(["Amount_Due", "Amount_Paid"])
        plt.show()







    # A bar graph with sub bars representing each expense type / category category for a year range {year 1 to year 2}.
        # Total expense in a category vs. year (for all categories, where each sub bar represents a category)
    # A pie chart which has slices representing expense in each expense type or category for a given year.




graph()









