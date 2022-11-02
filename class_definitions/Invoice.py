"""
Program: Invoice.py
Author: Alex Heinrichs
Date Created: 11/2/2022

Contains a class named Invoice and driver code to work it
"""


class Invoice:
    """Invoice Class"""

    def __init__(self, iid, cid, lname, fname, number, addy, iwp=dict()):
        self.invoice_id = iid
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = number
        self.address = addy
        self.items_with_price = iwp

    def __str__(self):
        return str(self.invoice_id) + ": " + str(self.customer_id) \
               + ": " + self.last_name + ", " + self.first_name \
               + " Phone: " + self.phone_number \
               + " Address: " + self.address \
               + " Items with price: " + str(self.items_with_price)

    def __repr__(self):
        if self.items_with_price == dict():
            return_string = 'Invoice({},{},{},{},{},{})'.format(self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)
        else:
            return_string = 'Invoice({},{},{},{},{},{}, {})'.format(self.invoice_id, self.customer_id, self.last_name, self.first_name, self.phone_number, self.address, self.items_with_price)
        return return_string

    def add_item(self, dict_item):
        self.items_with_price.update(dict_item)

    def create_invoice(self):
        total = 0.0
        for i, p in self.items_with_price.items():
            total += p
            print('{}.....${}'.format(i, str(p)))
        tax = total * .06
        total += tax
        print('Tax......... ${}'.format(str(round(tax, 2))))
        print('Total.......${}'.format(str(round(total, 2))))


# Driver
if __name__ == '__main__':
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
