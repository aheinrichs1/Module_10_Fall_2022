"""
Program: Customer.py
Author: Alex Heinrichs
Date Created: 11/2/2022

Contains a Customer class and driver code for practice with classes
"""

class Customer:
    def __init__(self, cid, lname, fname, pnumber, addy):
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber
        self.address = addy

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)


# driver
if __name__ == "__main__":
    cust1 = Customer('11', 'Heinrichs', 'Alex', '6416919494', '123 lane')
    cust1.display()
