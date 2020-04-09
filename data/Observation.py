from data.ObservationDate import ObservationDate


class Observation(object):
    def __init__(self, date_, value_):
        assert isinstance(date_, ObservationDate)
        self._obsDate = date_
        self._value = value_

    @property
    def obsDate(self):
        return self._obsDate

    @property
    def value(self):
        return self._value

    def __str__(self):
        return '[obsDate = {0}, value = {1}]'.format(self._obsDate, self._value)
