# TODO CHECK HOW PROF WANTS INPUTS FROM COMMANDLINE



import calendar
import datetime
import random
import re
import sys
import csv
import os



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

# checking for command line arguments
if len(sys.argv) < 4:
    print("Not enough parameters provided.")
    exit(0)
else:

    # getting the variables from the command line prompt
    year1_data = sys.argv[1]
    year1_temp = re.search(r'\-(.*)', year1_data)
    try:
        year1 = int(year1_temp.group(1))
        if year1 < 1980 or year1 > (datetime.date.today().year):
            print("Can't generate data before 1980 or after the current year.")
            exit(0)
    except ValueError:
        print("Can't input an invalid year.")

    year2_data = sys.argv[2]
    year2_temp = re.search(r'\-(.*)', year2_data)
    try:
        year2 = int(year2_temp.group(1))
        if year2 < 1980 or year2 > (datetime.date.today().year):
            print("Can't generate data before 1980 or after the current year.")
            exit(0)
    except ValueError:
        print("Can't input an invalid year.")

    filename_data = sys.argv[3]
    filename_data_temp = re.search(r'\-(.*)', filename_data)
    filename = str(filename_data_temp.group(1))

# for loop for the years
years_length = (year2 - year1) + 1
for i in range(0, years_length):
    working_year = year1 + i
    year_filename = str(working_year) + "MonthlyExpenses.csv"

    # empty array and add header to array
    file_array = []
    file_array.append(Header)

    # for loop for the months
    for month in range(1, 13):

        # for loop of all of the categories
        categ_list = list(Expense_Dict.keys())
        name_list = list(Expense_Dict.values())
        for categ_count in range(len(categ_list)):

            # for loop of all the names in each category
            exp_name = Expense_Dict[categ_list[categ_count]]
            for name in exp_name:
                if name == "House1" or name == "House2":
                    category = categ_list[categ_count]
                    amount_due = round(random.uniform(1000.0, 2000.0), 2)
                elif name == "Water":
                    category = categ_list[categ_count]
                    amount_due = round(random.uniform(20.0, 90.0), 2)
                elif name == "Internet":
                    category = categ_list[categ_count]
                    amount_due = round(random.uniform(5.0, 50.0), 2)
                elif name == "Power":
                    category = categ_list[categ_count]
                    amount_due = round(random.uniform(70.0, 110.0), 2)
                elif name == "Amex":
                    category = categ_list[categ_count]
                    amount_due = round(random.uniform(600.0, 1800.0), 2)
                else:
                    category = categ_list[categ_count]
                    amount_due = round(random.uniform(20.0, 110.0), 2)

                # finding rand due date w/in month
                rand_day = random.randint(1, 29)
                rand_due_date = str(month) + "/" + str(rand_day) + "/" + str(working_year)

                # randomly choosing to pay the payment or not
                assign = random.randint(0, 3)
                if assign == 0:
                    amt_paid = ""
                    rand_pay_date = ""
                    rand_meth = ""
                else:
                    amt_paid = amount_due
                    rand_day2 = random.randint(rand_day, 29)
                    rand_pay_date = str(month) + "/" + str(rand_day2) + "/" + str(working_year)
                    rand_meth = random.choice(Payment_Method)

                # storing random expense data in a list and appending it to file_array
                each_row = [working_year, calendar.month_name[month], category, name, amount_due, rand_due_date,
                            amt_paid, rand_pay_date, rand_meth]
                file_array.append(each_row)

    # putting year data in existing or new file
    current_folder = os.path.dirname(os.path.abspath(__file__))
    insert_filename = current_folder + "\\AnnualExpenseData\\" + year_filename
    try:
        with open(insert_filename, 'a', newline='') as file:
            add = csv.writer(file)
            add.writerows(file_array)
    except FileNotFoundError:
        with open(insert_filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(file_array)

print("Expense Data Generated")