"""

Program: employee.py
Author: Alex Heirnichs
Date created: 11/2/2022

Contains a class called employee which demonstrates encapsulation
"""
import datetime


class Employee:
    """Employee Class"""

    # Constructor
    def __init__(self, lname, fname, addy, phone_number, salaried, start_date, salary):
        self._last_name = lname
        self._first_name = fname
        self._address = addy
        self._phone = phone_number
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    def display(self):
        if self._salaried:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" \
                             + self._address + "\nSalaried employee: $" \
                             + str(self._salary) + "/year\nStart date: " \
                             + self._start_date.strftime("%m-%d-%Y")
        else:
            display_string = str(self._first_name) + " " + str(self._last_name) + "\n" \
                             + self._address + "\nHourly employee: $" \
                             + str(self._salary) + "/hour\nStart date: " \
                             + self._start_date.strftime("%m-%d-%Y")
        return display_string

    def __str__(self):
        return "First name: " + self._first_name \
                + "\nLast name: " + self._last_name \
                + "\nAddress: " + self._address \
                + "\nPhone number: " + self._phone \
                + "\nSalaried: " + str(self._salaried) \
                + "\nStart date: " + self._start_date.strftime("%m-%d-%Y") \
                + "\nSalary: " + str(self._salary)

    def __repr__(self):
        return "First name: " + self._first_name \
                + "\nLast name: " + self._last_name \
                + "\nAddress: " + self._address \
                + "\nPhone number: " + self._phone \
                + "\nSalaried: " + str(self._salaried) \
                + "\nStart date: " + self._start_date.strftime("%m-%d-%Y") \
                + "\nSalary: " + str(self._salary)


if __name__ == "__main__":
    start = datetime.datetime(2018, 5, 15)
    emp = Employee("Heinrichs", "Alex", "317 East St.\nAmes, Iowa",
                   "641-691-9494", False, start, 12.25)
    print(emp.display())
    print(emp)
    del emp
