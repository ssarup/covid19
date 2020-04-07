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

    def __init__(self, value_):
        assert isinstance(value_, datetime.datetime)
        self._value = value_

    def __str__(self):
        if self._value is None:
            return "[]"
        else:
            return "[value = {0}]".format(self._value.strftime('%m/%d/%Y'))

