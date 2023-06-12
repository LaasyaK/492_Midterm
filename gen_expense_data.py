# takes arguments: python gen_expense_data.py -Year1 <Start year> -Year2 <End Year> -folder <foldername>
# TODO HOW TO TAKE ARUGMENTS FOR YEARS
# TODO TEST HOW THE YEARS ARE PUT INTO EXCELS
# TODO CHECK THE LOGICAL #S FOR EACH COLUM

import csv
import calendar
import random
import re


# getting the header, expense_category, names, and payment_method info from DefaultsRecord
with open("DefaultsRecord.txt", 'r', newline='') as defaults:
    content = defaults.read()
    groups = re.findall(r'\[(.*?)\]', content)
    header = groups[0]
    Expense_category = groups[1]
    Expense_name = groups[2]
    Payment_Method = groups[3]

year1 = 2012
year2 = 2014


# for loop for the years
years_length = (year2 - year1) + 1
for i in range(0, years_length):
    working_year = year1 + i
    year_filename = str(working_year) + "MonthlyExpenses.csv"

    # empty array and add header to array
    file_array = []
    file_array.append(header)

    # for loop for the months
    for month in range(1, 13):

        # for loop for all of the expense_names
        for name_count in range(0, 6):

            # associating an expense_name to an expense_category and amount_due
            name = Expense_name[name_count]
            if name == "House1" or name == "House2":
                category = "Mortgage"
                amount_due = round(random.uniform(1000.0, 2000.0), 2)
            elif name == "Water":
                category = "Utility"
                amount_due = round(random.uniform(20.0, 90.0), 2)
            elif name == "Internet":
                category = "Utility"
                amount_due = round(random.uniform(5.0, 50.0), 2)
            elif name == "Power":
                category = "Utility"
                amount_due = round(random.uniform(70.0, 110.0), 2)
            elif name == "Amex":
                category = "CCBill"
                amount_due = round(random.uniform(1000.0, 2000.0), 2)
            else:
                category = "Misc"

            # finding rand due date w/in month
            rand_day = random.randint(1, 29)
            rand_due_date = str(month) + "/" + str(rand_day) + "/" + str(working_year)

            # randomly assigning amount_paid or not
            assign = random.randint(0, 3)
            if assign == 0:
                amt_paid = ""
            else:
                amt_paid = amount_due

            # randomly assign payment_date or empty
            assign = random.randint(0, 3)
            if assign == 0:
                rand_pay_date = ""
            else:
                rand_day = random.randint(1, 29)
                rand_pay_date = str(month) + "/" + str(rand_day) + "/" + str(working_year)

            # randomly getting a payment_method
            rand_meth = random.choice(Payment_Method)

            # storing random expense data in a list and appending it to file_array
            each_row = [working_year, calendar.month_name[month], category, name, amount_due, rand_due_date,
                        amt_paid, rand_pay_date, rand_meth]
            file_array.append(each_row)

    # putting year data in existing or new file
    try:
        with open(year_filename, 'a', newline='') as file:
            add = csv.writer(file)
            add.writerows(file_array)
    except FileNotFoundError:
        with open(year_filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(file_array)