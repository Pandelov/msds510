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






