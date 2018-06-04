import datetime


class Avenger:
    def _init_(self, record):
        """
        Initializes the object

        Args:
            record (dict) : Dictionary-based record
        """
        self.record = record

    def url(self):
        """
        Returns:
            str:URL
        """
        return self.record.get('url')

    def name_alias(self):
        """
        Returns:
            str:Name or alias of the character
        """
        return self.record.get('name_alias')

    def appearances(self):
        """
        Returns:
            int: How many times that character
            appears
        """
        return int(self.record.get('appearances'))

    def is_current(self):
        """
        Returns:
            bool: Is it still active? (True/False)
        """

        if self.record.get('is_current') == YES
            return true
        else
            return false

    def gender(self):
        """
        Returns:
            str: The gender of the character
        """
        return self.record.get('gender')

    def year(self):
        """
        Returns:
            int: The year when the character became a member of the Avengers
        """
        return int(self.record.get('year'))

    def date_joined(self):
        """
        Returns:
            datetime.date: The date the character joined the Avengers
        """

    def days_since_joining(self):
        """
        Returns:
            int: The number of days since the character joined
        """
        return int(self.record.get('days_since_joining'))

    def years_since_joining(self):
        """
        Returns:
            int: The number of years since the character joined
        """
        return int(self.record.get('years_since_joining'))

    def notes(self):
        return self.record.get('notes')

    def death_1(self):
        return self.record.get('death1')

    def death_2(self):
        return self.record.get('death2')

    def death_3(self):
        return self.record.get('death3')

    def death_4(self):
        return self.record.get('death4')

    def death_5(self):
        return self.record.get('death5')

    def honorary_member(self):
        return self.record.get('honorary')

    def return_1(self):
        return self.record.get('return1')

    def return_2(self):
        return self.record.get('return2')

    def return_3(self):
        return self.record.get('return3')

    def return_4(self):
        return self.record.get('return4')

    def return_5(self):
        return self.record.get('return5')

    def _str_(self):
        return self.record.get('_str_')

    def _repr_(self):
        return self.record.get('_repr_')
