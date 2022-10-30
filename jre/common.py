from datetime import date

class Date(date):
    """Class to store date information

    Attributes:
        year (int): Year of date
        month (int): Month of date
        day (int): Day of date
    """

    def __init__(self, year: int, month: int, day: int):
        """Initialize Date object

        Args:
            year (int): Year of date
            month (int): Month of date
            day (int): Day of date
        """
        super().__init__()

    @property
    def quarter(self):
        """int: Quarter of date
        """
        return self.month // 4 + 1