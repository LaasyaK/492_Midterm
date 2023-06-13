# *** DONE ***

import re


# getting the header, expense_category, names, and payment_method info from DefaultsRecord
with open("DefaultsRecord.txt", 'r', newline='') as defaults:
    content = defaults.read()
    groups = re.findall(r'(\[.*?\])', content)
    header = groups[0]
    Payment_Method = groups[1]
    Payment_Method = eval(Payment_Method)
    groups = re.findall(r'({.*?})', content)
    Expense_dict = groups[0]
    Expense_dict = eval(Expense_dict)
    Expense_Category = list(Expense_dict.keys())
    Expense_Name = list(Expense_dict.values())


# adding an expense category, expense name, or payment method to the defaults
def add_categ_name_method():
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
            print("\nThese are the current Expense_Categories and Expense_Names in a dictionary: ")
            print(Expense_dict)
            categ_add = input("What Category do you want to add? (or type 'main' to return to the main menu.) : ")
            if categ_add == "main":
                return 0
            name_add = input("What Name do you want to add to that Category? (or type 'main' to return to the main "
                             "menu.) : ")
            if name_add == "main":
                return 0
            Expense_dict.update({categ_add: [name_add]})
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

                # asking for name
                name = input("What Name do you want to add to that Category? (or type 'main' to return to the main "
                             "menu.) : ")
                if name == "main":
                    return 0
                temp_list = Expense_Name[int(categ)] + [name]
                Expense_dict[Expense_Category[int(categ)]] = temp_list
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
            no_error = False

        else:
            print("Can't input an input that isn't the associated 1 digit number, try again.\n")

        # put the changed variables into the DefaultsRecord
        with open("DefaultsRecord.txt", 'w', newline='') as writer:
            writer.write("header = " + str(header) + "\n")
            writer.write("Payment_Method = " + str(Payment_Method) + "\n")
            writer.write("Expense_dict = " + str(Expense_dict) + "\n")