from __future__ import print_function
import Pyro4
from  tabulate import tabulate
import random

@Pyro4.expose

class estate_agency(object):
    # Properties currently stored in the estate agency system.
    def __init__(self):
        self.properties =[[1,"For Sale" , "Richard","cf24 7yt",10, 2005],[2, "Sold","Naeima", "cf10 9nq",25, 2006],
        [3, "For Sale","luke", "cf90 4sa", 16, 2007], [4, "For Sale", "Kian", "cf23 5xa", 40, 2008], 
        [5, "Sold","Aline", "cf60 5tr", 4, 2009],[6,"Sold","Knar", "cf14 2py", 5, 2015]]

    # Displaying all six pieces of information relatinng to the set of properties currently stored in the estate agency system.
    def display_properties(self):
        return tabulate(self.properties, headers= ["ID", "Status", "Owner", "Postcode", "Number", "Construction Year" ])
    
    # Adding a property to the set of properties currectly stored.
    def add_property(self,owner,postcode,number,year):
        for i in self.properties:
            i[0] = id(i[0])
            ID = id(len(i))
            ID+=int(i[0])
         # setting the ID for the new property to be unique and sequencial.
        for s in self.properties:
            status = int(1) # setting the status of the new property, which should have a status for sale.
            if status is 1: # setting the binary indicator(0/1) for property status )
                status = "For Sale"
            elif status is 0:
                status = "Sold"
        property= [ID, status] # adding property data to the this list to complete the six pieces of information.
        property.append(owner)
        property.append(postcode)
        property.append(number)
        property.append(year)    
        self.properties.append(property) #adding the new property to  the set of properties currently stored in the estate agency system.
        # printing data in a table format with headers. 
        return tabulate(self.properties, headers = ["ID", "Status", "Owner", "Postcode", "Number", "Construction Year"])
         
    # Displaying the subset of properties currently stored as per the client construction years input range.
    def select_by_year(self, start_year, end_year):
        Years= [property for property in self.properties if int(start_year) <= int(property[-1]) <= int(end_year)+1]
        return tabulate(Years)

    # Displaying the subset of properties currently stored as client's postcode choice.
    def select_by_postcode(self, postcode):
        for i in self.properties:
            sublist=[  ]
            if postcode in i:
                sublist.append(i)
                return tabulate(sublist)
                
    # Setting the status of the property specified by postcode and (house/apartment) number to " For-Sale"
    def set_for_sale(self, postcode, number):
        for i in self.properties:
            if i[3] == postcode and i[4] == int(number):
                i[1] = "FOR-SALE" 
                return i
                
     # Setting the status of the property specified by postcode and (house/apartment) number to " NOT FOR SALE"
    def set_not_sale(self, postcode, number):
        for j in self.properties:
            if j[3] == postcode and j[4] == int(number):
                j[1] = "NOT-FOR-SALE" 
                return j

     # Displaying all six pieces of information relatinng to the set of properties currently stored by year of construction.
    def display_properties_sorted(self):
        self.properties.sort(key=lambda x: int(x[-1])) # sort by the construction year.
        return tabulate(self.properties, headers= ["ID", "Status", "Owner", "Postcode", "Number", "Construction Year" ])


def main():
    Estate_agency = estate_agency()
    
    Pyro4.Daemon.serveSimple(
        {
            Estate_agency: "object.agency"
        },
        ns=True)


if __name__ == "__main__":
    main()





