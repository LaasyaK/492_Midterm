This Repository holds all the files needed to run an Expense Tracking program.
This program has multiple functions:
  - The Main Menu can be run as 'manageExpenses.py' and it can:
      - Add an expense to a current CSV of expenses for a year or create a new CSV and record that expense
      - Search through all the available expenses in a folder and filter them based on a user search criteria and print them to the user
      - Modify a record found by searching and changing a field of information
      - Add a Default Category, Name, or Payment Method to the program
  - The Reports Menu can be run as 'manageExpenses.py --report' and it can:
      - Create a text or CSV of an annual summed expense category or name for many years
      - Create a text or CSV of annual summed expenses for all the names under a category for many years
      - Create a text or CSV of summed monthly expenses for a year
  - The Graphs Menu can be run as 'manageExpenses.py --graph' and it can:
      - Show a bar graph of an annual summed expense categories or names for many years
      - Show a bar graph of annual summed expense categories for many years
      - Show a pie chart of annual summed expenses for categories or names for a year
      - Show a bar graph of summed monthly expenses for a year
  - Fake user data can be generated as 'gen_expense_data.py -year1 startYear -year2 endYear -folder folderName' and it:
      - creates multiple CSV files for each year from the startYear to the endYear inclusively of random user data containing:
          - year, month, expense_category, expense_name, amount_due, due_date, amount_paid, payment_date, and payment_method
      - startYear, endYear, and folderName are command line arugments that determine the range of years and where the CSV files will be located

This program was written for the ECE 492 Python in Engineering class.
Author: Laasya Kallepalli,
Date: 6/23/2023
