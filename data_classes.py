# ------------------------------------------------------------------------------------- #
# Title: Data Classes Module
# # Description: A collection of data classes for managing the application
# ChangeLog:
# WMarcus 3/19/2025, Created Script
# -------------------------------------------------------------------------------------- #
from datetime import date
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - WMarcus, 3/23/25, Created class
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        This function initiates the class Person and names each instance of its attributes.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        This function holds and returns the first name of the individual, capitalized.
        
        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        This function validates the individual's first name for alphabetical content.
        
        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """
        This function holds and returns the last name of the individual, capitalized.
        
        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        This function validates the individual's last name for alphabetical content.
        
        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """
        This function overrides the ___str___() function to contain the requisite data.
        
        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - WMarcus, 3/23/2025, Created Class
    """
    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 1):
        """
        This function initiates the class Employee and names each instance of its attributes.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        super().__init__(first_name=first_name,last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        This function holds and returns the review date of the individual.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        This function validates the review date against the correct format.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        This function holds and returns the review rating of the individual.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        """
        This function validates the review rating of the individual against the accpetable ratings.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        """
        This function overrides the __str__ function with the requisite data.

        ChangeLog:
        WMarcus, 3/23/25, Created Function
        """
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
