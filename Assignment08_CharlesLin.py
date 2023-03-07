# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog: Charles Lin 2023-03-04
# CLin, 2023-03-04 Created file
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name_str = 'products.txt' # The name of the data file
file_obj = None  # An object that represents a file
table_lst = [] # A list that acts as a 'table' of rows
choice_str = "" # Captures the user option selection

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
        to_string: returns product's name and price data as a string
    changelog:
        CLin, 2023-03-04,Created Class
    """

    # TODO: Add Code for Product class (Constructor, Properties, & Methods)
    # --Constructor--
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # --Properties--
    @property
    def product_name(self): # getter
        return str(self.__product_name).title() # Format attribute as Title case

    @product_name.setter
    def product_name(self, value): # setter
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception ("Product names cannot be numbers")

    @property
    def product_price(self): # getter
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value): # setter
        if str(value).isnumeric() == True:
            self.__product_price = value
        else:
            raise Exception ("Product price has to be numbers")

    def to_string(self):
        """  Returns object data in a comma separated string of values

        ;return; (string) CSV data
        """
        object_data_csv = self.product_name + ',' + self.product_price
        return object_data_csv

# Look at what the class does
# objP1 = Product("Desk", "99")
# print(objP1.to_string())

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class Processor:
    """Processes data to and from a file and a list of product objects:

    methods:

        read_data_from_file(file_name): -> (a list of product objects)
        add_data_to_list(product_name, product_price, list_of_rows):
        write_data_to_file(file_name, list_of_product_objects):

    changelog: (When,Who,What)
        CLin,2023-03-04,Created Class
    """

    #  TODO: Add Code to process data from a file

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try:    # try/except to ask folks to place a starting product list file if it doesn't exist
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"product_name": task.strip(), "product_price": priority.strip()}
                list_of_rows.append(row)
            file.close()
            return list_of_rows
        except:
            print()
            print("Such file doesn't exist. Please place product.txt file in the working folder.")
            print()

    #  TODO: Add Code to process data to a file

    @staticmethod
    def add_data_to_list(product_name, product_price, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param product_name: (string) with name of product:
        :param product_price: (int) with price of product:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"product_name": str(product_name).strip(), "product_price": int(product_price)}
        list_of_rows.append({"product_name": product_name, "product_price": product_price})
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        objFile = open(file_name_str, "w")
        for row in list_of_rows:
            objFile.write(str(row["product_name"]) + ',' + str(row["product_price"] + '\n'))
        objFile.close()
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output

    methods:
        output_menu_products():

        output_current_products_in_list(list_of_rows):

        input_menu_choice():

    changelog: (When,Who,What)
        CLin,2023-03-04,Created Class:
    """
    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def output_menu_products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Data
        2) Add a New Item
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_products_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for row in list_of_rows:
            print(row["product_name"] + " (" + row["product_price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """  Gets product and price values to be added to the list

        :return: (string, int) with product and price
        """
        # TODO: Add Code Here!
        product_name = str(input("Product to add: ")).strip().title()
        product_price = str(input("Price in integer: ")).strip()
        print()
        return product_name, product_price


# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data

while (True):
    # Show the menu
    IO.output_menu_products()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Show user current data in the list of product objects
    if choice_str.strip() == '1':  # Show current data
        IO.output_current_products_in_list(list_of_rows=table_lst)  # Show current data in the list/table
        continue  # to show the menu

    # Let user add data to the list of product objects
    elif choice_str.strip() == '2':  # Add a new Task
        product_name, product_price = IO.input_new_product_and_price()
        objP1 = Product(product_name,product_price)
        table_lst = Processor.add_data_to_list(product_name=product_name, product_price=product_price, list_of_rows=table_lst)
        continue  # to show the menu

    # let user save current data to file and exit program
    elif choice_str.strip() == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Products written to file!")
        print()
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        print()
        break  # by exiting loop

    else:
        print("Please choose 1, 2, 3, or 4")
        print()

# Main Body of Script  ---------------------------------------------------- #
