# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# WMarcus, 3/23/25, Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):
    """
    A class to test the constructor, first/last name validation, and __str__() of Person
    Changelog:
    Wmarcus, 3/23/25, Created class
    """
    def test_person_init(self):  # Tests the constructor
        """
        This function tests the initiator of Person.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        person = Person("Johnny", "Snow")
        self.assertEqual(person.first_name, "Johnny")
        self.assertEqual(person.last_name, "Snow")

    def test_person_invalid_name(self):  # Test the first and last name validations
        """
        This function tests the first name and last name validation.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        with self.assertRaises(ValueError):
            person = Person("123", "Snow")
        with self.assertRaises(ValueError):
            person = Person("Johnny", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        """
        This function tests the override of __str__.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        person = Person("Johnny", "Snow")
        self.assertEqual(str(person), "Johnny,Snow")


class TestEmployee(unittest.TestCase):
    """
    A class to test the constructor, review_date and review_rating validation, and __str__() of Employee
    ChangeLog:
    WMarcus, 3/23/25, Created Class
    """
    def test_employee_init(self):
        """
        This function tests the constructor of Employee.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        employee = Employee("Bad", "Horse", "2008-07-15", 1)
        self.assertEqual(employee.first_name, "Bad")
        self.assertEqual(employee.last_name, "Horse")
        self.assertEqual(employee.review_date, "2008-07-15")
        self.assertEqual(employee.review_rating, 1)

    def test_employee_invalid_review_date(self):
        """
        This function tests the review date validation.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        with self.assertRaises(ValueError):
            student = Employee("Neil", "Harris", "2008-7-15", 5)

    def test_employee_invalid_review_rating(self):
        """
        This function tests the review rating validation.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        with self.assertRaises(ValueError):
            student = Employee("Nathan", "Fillion", "2008-07-15", "five")

    def test_employee_str(self):
        """
        This function tests the __str__ function of Employee.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        employee = Employee("Felicia", "Day", "2008-07-15", 5)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "Felicia,Day,2008-07-15,5")

if __name__ == '__main__':
    unittest.main()