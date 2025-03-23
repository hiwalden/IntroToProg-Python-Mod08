# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog:
# WMarcus, 3/23/25, Created Script
# ------------------------------------------------------------------------------- #


import unittest
import tempfile
import json
import data_classes as data
from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        """
        This function creates a temporary file for testing purposes.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        """
        This function deletes the temporary file.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_data_from_file(self):
        """
        This function tests the successful reading of file, and translation to objects.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "Neil", "LastName": "Harris", "ReviewDate":"2008-07-15", "ReviewRating":5},
            {"FirstName": "Nathan", "LastName": "Fillion", "ReviewDate": "2008-07-15", "ReviewRating": 5}
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, employee_type=Employee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "Neil")
        self.assertEqual(self.employee_data[0].last_name, "Harris")
        self.assertEqual(self.employee_data[0].review_date, "2008-07-15")
        self.assertEqual(self.employee_data[0].review_rating, 5)
        self.assertEqual(self.employee_data[1].first_name, "Nathan")
        self.assertEqual(self.employee_data[1].last_name, "Fillion")
        self.assertEqual(self.employee_data[1].review_date, "2008-07-15")
        self.assertEqual(self.employee_data[1].review_rating, 5)

    def test_write_data_to_file(self):
        """
        This function tests the writing of objects to JSON using sample objects.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        # Create some sample student objects
        sample_employees = [
            data.Employee("Neil", "Harris", "2008-07-15", 5),
            data.Employee("Nathan", "Fillion", "2008-07-15", 5)
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]["FirstName"], "Neil")
        self.assertEqual(file_data[0]["LastName"], "Harris")
        self.assertEqual(file_data[0]["ReviewDate"], "2008-07-15")
        self.assertEqual(file_data[0]["ReviewRating"], 5)
        self.assertEqual(file_data[1]["FirstName"], "Nathan")
        self.assertEqual(file_data[1]["LastName"], "Fillion")
        self.assertEqual(file_data[1]["ReviewDate"], "2008-07-15")
        self.assertEqual(file_data[1]["ReviewRating"], 5)

if __name__ == "__main__":
    unittest.main()
