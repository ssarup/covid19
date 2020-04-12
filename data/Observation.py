from data.ObservationDate import ObservationDate
from math import log


class Observation(object):
    def __init__(self, date_, value_):
        assert isinstance(date_, ObservationDate)
        self._obsDate = date_
        self._value = value_
        if value_ <= 0:
            self._log2Value = None
            self._lnValue = None
        else:
            self._log2Value = log(self._value, 2)
            self._lnValue = log(self._value)

    @property
    def obsDate(self):
        return self._obsDate

    @property
    def value(self):
        return self._value

    @property
    def log2Value(self):
        return self._log2Value

    @property
    def lnValue(self):
        return self._lnValue

    def __str__(self):
        return '[obsDate = {0}, value = {1}]'.format(self._obsDate, self._value)
