class Avenger:
    def _init_(self, record):
        """
        Initializes the object with a dictionary-based record.

        Args:
            record (dict) : Dictionary-based record of Avenger data
        """
        self.record = record

    def url (self):
        return self.record.get('url')

    def name_alias(self):
        return self.record.get('name_alias')

    def appearances(self):
        return int(self.record.get('appearances'))

    def is_current(self):
        if self.record.get('is_current')==YES
            return true
        else
            return false

    def gender(self):
        return self.record.get('gender')

    def year(self):
        return int(self.record.get('year'))

    def date_joined(self):

    def days_since_joining(self):
        return int(self.record.get('days_since_joining'))

    def years_since_joining(self):
        return int(self.record.get('years_since_joining'))

    def notes(self):
        return self.record.get('notes')

    def _str_(self):
        return self.record.get('_str_')

    def _repr_(self):
        return self.record.get('_repr_')






