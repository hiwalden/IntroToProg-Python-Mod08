# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# WMarcus, 3/23/25, Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    """
    Tests the menu choice input, and employee data input
    ChangeLog:
    WMarcus, 3/23/25, Created Class
    """
    def setUp(self):
        """
        This function establishes a list for the purposes of testing.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        self.employee_data = []

    def test_input_menu_choice(self):
        """
        This function tests the recognition of menu input.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        """
        This function tests the recognition of Employee data input.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        with patch('builtins.input', side_effect=['Doctor', 'Horrible', '2008-07-15', 1]):
            IO.input_employee_data(self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'Doctor')
            self.assertEqual(self.employee_data[0].last_name, 'Horrible')
            self.assertEqual(self.employee_data[0].review_date, '2008-07-15')
            self.assertEqual(self.employee_data[0].review_rating, 1)

        # Simulate invalid date input
        with patch('builtins.input', side_effect=['Captain', 'Hammer', 'invalid', 5]):
            IO.input_employee_data(self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

        # Simulate invalid rating input (not an int)
        with patch('builtins.input', side_effect=['Captain', 'Hammer', '2008-07-15', 'invalid']):
            IO.input_employee_data(self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()