import datetime


class ObservationDate(object):

    @classmethod
    def fromMDY(cls, mdY_):
        """Verifies input mdY_ string."""
        try:
            assert isinstance(mdY_, str)
            return ObservationDate(datetime.datetime.strptime(mdY_, '%m/%d/%Y'))
        except:
            return None

    @classmethod
    def fromMDY2(cls, mdy_):
        """
        Verifies input mdy_ string.
        This function assumes its a 2-digit year.
        """
        try:
            assert isinstance(mdy_, str)
            return ObservationDate(datetime.datetime.strptime(mdy_, '%m/%d/%y'))
        except:
            return None

    def __init__(self, value_):
        assert isinstance(value_, datetime.datetime)
        self._value = value_

    @property
    def value(self):
        return self._value

    def __str__(self):
        if self._value is None:
            return "[]"
        else:
            return "[value = {0}]".format(self._value.strftime('%m/%d/%Y'))

