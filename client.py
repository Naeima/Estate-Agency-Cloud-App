from __future__ import print_function
import sys
import pandas as pd
if sys.version_info < (3, 0):
    input = raw_input


class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, estate_agency):
        print("This is {0}.".format(self.name))
        print("The Estate Agency contains: ")
        self.display_properties(estate_agency)
        self.add_property(estate_agency)
        self.select_by_year(estate_agency)
        self.select_by_postcode(estate_agency)
        self.set_for_sale(estate_agency)
        self.set_not_sale(estate_agency)
        self.display_properties_sorted(estate_agency)
        print("Thank you, come again!")

    def display_properties(self, estate_agency):
        print(estate_agency.display_properties())  
        
    def add_property(self, estate_agency):
        owner = input("Type the Owner of the property to add: ").strip()
        postcode= input("Type the Postcode of the property : ").strip()
        number = input("Type the property Number: ")
        year= input("Type the property Construction Year: ")
        #status = int(input("Enter 1 if it's For Sale or  0 if it's Sold:  "),2) # input is binary, 0 or 1.
        if (owner, postcode, number, year):
            print(estate_agency.add_property(owner, postcode, number, year))
        
        
    def select_by_year(self, estate_agency):
        start_year = input("Enter the start year: ").strip()
        end_year = input("Enter the end year: ").strip()
        if start_year and end_year:    
            print(estate_agency.select_by_year(start_year, end_year))
    
    def select_by_postcode(self, estate_agency):
        postcode = input("Enter the postcode as formatted above: ")
        if postcode:
            print(estate_agency.select_by_postcode(postcode))

    def set_for_sale(self, estate_agency):
        postcode = input("Enter the postcode as formatted to set for sale: ")
        number =input("Type the property Number to set for sale: ")
        if postcode and number:
            print(estate_agency.set_for_sale(postcode, number))

    def set_not_sale(self, estate_agency):
        postcode = input("Enter the postcode as formatted to set NOT for sale: ")
        number =input("Type the property Number to set NOT for sale: ")
        if postcode and number:
           print(estate_agency.set_not_sale(postcode, number))

    def display_properties_sorted(self, estate_agency):
        print(estate_agency.display_properties_sorted())
            
    #         #estate_agency.set_for_sale(postcode,number)

